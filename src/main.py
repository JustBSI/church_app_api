from fastapi import FastAPI
from src.groups.router import router as router_group
from src.persons.router import router as router_person
from src.records.router import router as router_record
from src.reports.router import router as router_report
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_cache.backends.redis import RedisBackend

app = FastAPI(
    title="Church App"
)


app.include_router(router_group)
app.include_router(router_person)
app.include_router(router_report)
app.include_router(router_record)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
