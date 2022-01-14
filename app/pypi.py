
from bs4 import BeautifulSoup
import requests
import markdown
import re


def parse_code_blocks(text):
    regex = r"```.*?```"
    matches = re.finditer(regex, text, re.DOTALL)
    occurences = []
    for m in matches:
        occurences.append(m.group())

    for o in occurences:
        lang = ""
        end = o.find("\n")
        lang = o[3:end]
        start = end + 1
        class_name = "language-bash"
        if lang:
            class_name = f"language-{lang}"
        # no-prose to avoid typography tailwind plugin to style code blocks
        # here we let highlight-js do the job
        code = o[start:-3].rstrip("\n")
        newblock = f"<pre><code class='{class_name}'>{code}</code></pre>"
        text = text.replace(o, newblock)
    return text

def has_masonite_classifier(classifiers):
    for classifier in classifiers:
        if classifier.startswith("Framework :: Masonite"):
            return True
    return False


def get_masonite_versions(classifiers):
    base_classifier = "Framework :: Masonite :: "
    versions = []
    for classifier in classifiers:
        if classifier.startswith(base_classifier):
            version_str = classifier.replace(base_classifier, "")
            versions.append(version_str)
    return versions


def find_packages():
    packages = []
    status_code = 200
    page = 1
    while status_code != 404:
        response = requests.get(f'http://pypi.org/search/?c=Framework+%3A%3A+Masonite&page={page}')
        status_code = response.status_code
        if status_code == requests.codes.ok:
            packages += parse_search_page(response.text)
            page += 1

    return packages

def parse_search_page(page_text):
    search_results = []
    soup = BeautifulSoup(page_text, 'html.parser')
    package_snippets = soup.find_all('a', class_='package-snippet')
    search_results = []
    for package_snippet in package_snippets:
        span_elems = package_snippet.find_all('span')
        name = span_elems[0].text.strip()
        search_results.append(name)
    return search_results


def get_package_data(package_name):
    """Fetch up to date package data on PyPi API + GitHub API for GitHub repos."""
    # get additional data
    pypi_response = requests.get(f"https://pypi.org/pypi/{package_name}/json/")
    if pypi_response.status_code != 200:
        print("ERROR: fetching additional packages details failed !")
        return None

    data = pypi_response.json()["info"]
    repo_url = data["home_page"]
    is_on_github = repo_url.startswith("https://github.com")

    # convert description to html if markdown
    if data["description_content_type"] == "text/markdown":
        # parse ```language ...``` block to <code></code>
        text = parse_code_blocks(data["description"])
        description = markdown.markdown(text)
    else:
        description = data["description"] or "N/A"

    stars = 0
    issues = 0
    license = 0
    # add meta if on github
    if is_on_github:
        github_repo =  repo_url.replace("https://github.com/", "")
        response = requests.get(f"https://api.github.com/repos/{github_repo}")
        if response.status_code == 200:
            github_data = response.json()
            if github_data.get("license"):
                license = github_data["license"].get("name")
            stars = github_data["stargazers_count"]
            issues = github_data["open_issues_count"]

    # get Masonite versions compatibility
    masonite_versions = get_masonite_versions(data["classifiers"])
    masonite_versions = ",".join(masonite_versions)

    is_official=False
    if data["home_page"].startswith("https://github.com/MasoniteFramework/"):
        is_official=True

    return {
        "stars": stars,
        "issues": issues,
        "license": license,
        "masonite_versions": masonite_versions,
        "description": description,
        "author": data["author"],
        "author_email": data["author_email"],
        "short_description": data["summary"] or "N/A",
        "description": description,
        "repository_url": data["home_page"],
        "version": data["version"],
        "pypi_url": data["package_url"],
        "is_official": is_official,
    }