from fastapi.applications import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from toolz import pipe


from app.routes import register_routers
from app.infrastructure.environment import Settings
from app.infrastructure.db import create_db_and_tables, init_db


def create_instance(settings: Settings) -> FastAPI:

    return {"app": FastAPI(
        docs_url=settings.BASE_PATH + '/docs', redoc_url=None, 
        openapi_url=settings.BASE_PATH + '/openapi.json',
        debug=settings.WEB_APP_DEBUG,
        title=settings.WEB_APP_TITLE,
        description=settings.WEB_APP_DESCRIPTION,
        version=settings.WEB_APP_VERSION,
        prefix=settings.BASE_PATH
    ), "settings": settings}

def init_database(app: FastAPI) -> FastAPI:
    # TODO init databases if applicable
    init_db()
    return app

def register_events(app: FastAPI) -> FastAPI:
    # TODO add events if applicable
    app.on_event("startup")(create_db_and_tables) # This event can be removed if not seeding a database

    return app


def register_middleware(config: dict) -> FastAPI:
    # TODO register middleware if applicable
    app = config.get("app")
    app.add_middleware(CORSMiddleware, 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
    
    return app

def register_exception_handlers(app: FastAPI) -> FastAPI:
    # TODO register exception handlers if applicable
    # Modify HttpExceptions to follow API guidelines
    return app
    

def init_app(settings: Settings) -> FastAPI:
    app: FastAPI = pipe(
        settings,
        create_instance,
        register_middleware,
        init_database,
        register_events,
        register_routers,
        register_exception_handlers,
    )
    return app
