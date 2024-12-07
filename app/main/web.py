from fastapi import FastAPI

from .di import init_sql_dependencies, init_nosql_dependencies
from .routers import init_routers


def create_sql_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_sql_dependencies(app)
    return app


def create_nosql_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_nosql_dependencies(app)
    return app
