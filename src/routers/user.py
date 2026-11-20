"""Роутер для работы с пользователями.

Данные хранятся в памяти, чтобы приложение оставалось простым:
для лабораторной работы важны не БД, а тесты и CI/CD-процесс.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

# Учебное «хранилище» пользователей
USERS: dict[int, dict] = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
}


class User(BaseModel):
    id: int
    name: str
    email: str


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    """Вернуть пользователя по id или 404, если его нет."""
    user = USERS.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user)
