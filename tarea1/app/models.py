from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class News(Base): 

    __tablename__ = "news"

    id_news = Column(Integer, primary_key=True, index=True)
    title = Column(String(300))
    url = Column(String(300))
    date = Column(String(20))
    media_outlet = Column(String(400))
    category =  Column(String(50))
