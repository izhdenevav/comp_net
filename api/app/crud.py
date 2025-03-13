from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from . import models
from .models import Anime
from .database import SessionLocal

def save_animes(anime_list):
    session = SessionLocal()
    for anime in anime_list:
        db_anime = Anime(
            russianname=anime["russianname"],
            animetype=anime["animetype"],
            releaseyear=anime["releaseyear"],
            cover=anime["cover"]
        )
        session.add(db_anime)
    session.commit()
    session.close()

def get_all_parsed_data(db: Session):
    return db.query(models.Anime).all()