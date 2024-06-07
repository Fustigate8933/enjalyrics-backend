from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, index=True)
    song_name = Column(String, index=True)
    artist = Column(String, index=True)
    lyrics = Column(String)

    highlights = relationship("Highlight", back_populates="song")


class Highlight(Base):
    __tablename__ = 'highlights'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    song_id = Column(Integer, ForeignKey('songs.id'))
    highlighted_text = Column(String)
    translation = Column(String)
    start_index = Column(Integer)
    end_index = Column(Integer)
    start_line = Column(Integer)
    end_line = Column(Integer)

    song = relationship("Song", back_populates="highlights")

