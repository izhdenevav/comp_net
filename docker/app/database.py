import asyncpg

DB_CONFIG = {
    "database": "animes",
    "user": "user",
    "password": "1",
    "host": "my_postgres",
    "port": "5432"
}

async def get_db():
    return await asyncpg.connect(**DB_CONFIG)