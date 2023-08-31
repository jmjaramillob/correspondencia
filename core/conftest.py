import pytest
from django.conf import settings


DEFAULT_ENGINE = "django.db.backends.postgresql_psycopg2"

"""
@pytest.fixture(scope="session")
def django_db_setup():
    \"""Fixture to set up the database for the tests.\"""
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
        "HOST": os.environ["DB_TEST_HOST"],
        "NAME": os.environ["DB_TEST_NAME"],
        "PORT": os.environ["DB_TEST_PORT"],
        "USER": os.environ["DB_TEST_USER"],
        "PASSWORD": os.environ["DB_TEST_PASSWORD"],

"""

@pytest.fixture(autouse=True, scope="session")
def django_language_setup():
    """Fixture to set up the language for the tests."""
    settings.LANGUAGE_CODE = "en-us"