"""Точка входа приложения FastAPI."""

from fastapi import FastAPI

from src.routers import user

app = FastAPI(title="Lab 5 CI/CD demo", version="1.0.0")

app.include_router(user.router)


@app.get("/")
def root() -> dict:
    """Простой health-check: удобно проверять контейнер после docker run."""
    return {"status": "ok", "service": "my-app"}
