rom sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, Date
from Domain.clients import Client
from Domain.rooms import Rooms

Base = declarative_base()