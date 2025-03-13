from sqlalchemy import Column, String, Integer
from .database import Base

class Anime(Base):
    __tablename__ = "anime_titles"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    russianname = Column(String)
    animetype = Column(String)
    releaseyear = Column(String)
    cover = Column(String)
