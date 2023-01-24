import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column (Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column (Integer, primary_key=True)
    user_from_id = Column(Integer,  ForeignKey('user.id'))
    user_to_id = Column(Integer,  ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column (Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column (Integer, primary_key=True)
    comment_text = Column(String(800))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column (Integer, primary_key=True)
    type = Column(Integer)
    url = Column(String)
    post_id = Column (Integer, ForeignKey('post.id') )
    post = relationship(Post)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')