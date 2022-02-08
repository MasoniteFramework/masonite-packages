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
    "mysql": db_url(options={"charset": "utf8mb4"}),
    "postgres": db_url(),
}

DB = ConnectionResolver().set_connection_details(DATABASES)
