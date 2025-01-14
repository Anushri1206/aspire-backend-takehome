from fastapi.applications import FastAPI

from app.routes import root
from app.infrastructure.environment import get_settings


def register_routers(app: FastAPI) -> FastAPI:
    settings = get_settings()
    app.router.prefix=settings.BASE_PATH

    app.include_router(root.router)

    return app