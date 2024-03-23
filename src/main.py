from fastapi import FastAPI

from src.groups.router import router as router_group
from src.persons.router import router as router_person

app = FastAPI(
    title="Church App"
)


app.include_router(router_group)
app.include_router(router_person)
# app.include_router(router_reports)
