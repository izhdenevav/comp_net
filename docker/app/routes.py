from fastapi import APIRouter, Query, Depends
# from .crud import save_animes
# from .parser import parse_animes
from .schemas import URLCreate, URLResponse
from .database import get_db

router = APIRouter()

@router.on_event("startup")
async def startup():
    conn = await get_db()
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id SERIAL PRIMARY KEY,
            url TEXT
        );
    """)
    await conn.close()

@router.post("/add", response_model=URLResponse)
async def add_url(data: URLCreate):
    conn = await get_db()
    rows = await conn.fetch("INSERT INTO urls (url) VALUES ($1) RETURNING id, url;", data.url)
    await conn.close()
    row = rows[0]
    print(row)
    return {"id": row["id"], "url": row["url"]}


@router.get("/get", response_model=list[str])
async def get_urls():
    conn = await get_db()
    rows = await conn.fetch("SELECT url FROM urls;")
    await conn.close()
    return [row["url"] for row in rows]



