from fastapi import FastAPI
from src.groups.router import router as router_group
from src.persons.router import router as router_person
from src.records.router import router as router_record
from src.reports.router import router as router_report

app = FastAPI(
    title="Church App"
)


app.include_router(router_group)
app.include_router(router_person)
app.include_router(router_report)
app.include_router(router_record)
