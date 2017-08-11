import os


# Development environment.
DEBUG = True

# Base directory.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Disable an expensive bit of the ORM.
SQLALCHEMY_TRACK_MODIFICATIONS = False

# A common configuration; one request thread, one background worker thread.
THREADS_PER_PAGE = 2

# Some defaults.
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"

# Override in local configs.
SQLALCHEMY_DATABASE_URI = ''

EDO_ORACLE_HOST = ''
EDO_ORACLE_PORT = ''
EDO_ORACLE_SID = ''
EDO_ORACLE_USERNAME = ''
EDO_ORACLE_PASSWORD = ''
