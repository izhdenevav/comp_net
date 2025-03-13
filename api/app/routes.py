from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from .crud import save_animes
from .parser import parse_animes
from .models import Anime
from .database import get_db

router = APIRouter()

@router.get("/parse")
def parse(url: str = Query(..., description="URL для парсинга")):
    animes = parse_animes(url)
    save_animes(animes)
    return {"message": f"Спарсено {len(animes)} аниме"}

@router.get("/animes")
def get_animes(db: Session = Depends(get_db)):
    print(Anime.__table__)
    animes = db.query(Anime).all()
    return [
        {
            "ID": anime.id,
            "Russian Name": anime.russianname,
            "Anime Type": anime.animetype,
            "Release Year": anime.releaseyear,
            "Cover": anime.cover
        }
        for anime in animes
    ]

