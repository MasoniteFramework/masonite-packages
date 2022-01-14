from tests import TestCase

from app.pypi import get_masonite_versions, has_masonite_classifier


class BasicTestCase(TestCase):
    def test_has_masonite_classifier(self):
        assert not has_masonite_classifier([""])
        assert not has_masonite_classifier(["Framework :: Django", "Python :: 3.10"])
        assert has_masonite_classifier(["Python :: 3.10", "Framework :: Masonite"])
        assert has_masonite_classifier(["Python :: 3.10", "Framework :: Masonite :: 4.0", "Framework :: Masonite :: 3.0"])

    def test_get_masonite_versions(self):
        assert not get_masonite_versions(["Python :: 3.10", "Framework :: Masonite"])
        versions = get_masonite_versions(["Python :: 3.10", "Framework :: Masonite :: 4.0", "Framework :: Masonite :: 3.0"])
        assert set(versions) == {"4.0", "3.0"}
