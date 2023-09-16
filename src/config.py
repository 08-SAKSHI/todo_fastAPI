from base64 import b64decode
from functools import lru_cache
from typing import Any, Dict, Optional

from pydantic import BaseSettings, Field, validator


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    SQLITE_DB_FILE: str = "todolist.db"  # SQLite database file name
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        db_file = values.get("SQLITE_DB_FILE")
        return f"sqlite:///{db_file}"  # SQLite connection URI

if __name__ == "__main__":
    settings = get_settings()
    print("SQLALCHEMY_DATABASE_URI:", settings.SQLALCHEMY_DATABASE_URI)
