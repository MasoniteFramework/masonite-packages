from masonite.environment import LoadEnvironment, env
from masoniteorm.connections import ConnectionResolver
from masoniteorm.config import db_url

#  Loads in the environment variables when this page is imported.
LoadEnvironment()

"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""
DATABASES = {
    "default": env("DB_CONNECTION", "sqlite"),
    "sqlite": {
        "driver": "sqlite",
        "database": "masonite_packages.sqlite3",
        "prefix": "",
        "log_queries": env("DB_LOG"),
    },
    "mysql": {
        "driver": "mysql",
        "host": env("DB_HOST"),
        "user": env("DB_USERNAME"),
        "password": env("DB_PASSWORD"),
        "database": env("DB_DATABASE"),
        "port": env("DB_PORT"),
        "prefix": "",
        "grammar": "mysql",
        "options": {
            "charset": "utf8mb4",
        },
        "log_queries": env("DB_LOG"),
    },
    "postgres": db_url(),
}

DB = ConnectionResolver().set_connection_details(DATABASES)
