from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    print("Создаём сессию БД...")
    db = SessionLocal()
    print("Сессия создана!")

    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)
