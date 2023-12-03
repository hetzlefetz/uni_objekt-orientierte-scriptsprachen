from kink import di

from helloworld.services.router import Router
from helloworld.services.sqlite_db_service import (
    SqliteDbService,
)


di["db_service"] = SqliteDbService()
di["router_service"] = Router()
