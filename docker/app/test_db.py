import asyncio 
import asyncpg

async def test_connection():
    try:
        conn = await asyncpg.connect(
            database="animes",
            user="user",
            password="1",
            host="my_postgres",
            port="5432"
        )
        print("Connected successfully!")
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(test_connection)