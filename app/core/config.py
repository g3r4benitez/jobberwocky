import os

from starlette.config import Config

ROOT_DIR = os.getcwd()
_config = Config(os.path.join(ROOT_DIR, ".env"))
APP_VERSION = "0.0.1"
APP_NAME = "Jobberwocky"
API_PREFIX = "/api"

# Env vars
IS_DEBUG: bool = _config("IS_DEBUG", cast=bool, default=False)
DB_URL: str = _config("DB_URL", cast=str)
EXTERNAL_SOURCE_URL: str = _config("EXTERNAL_SOURCE_URL", cast=str)