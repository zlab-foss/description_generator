from sqlalchemy import Boolean, Column, Integer, String, Float 
from sqlalchemy.dialects.postgresql import ARRAY

from .database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    description = Column(String)
    type_id = Column(Integer, nullable=False)
    available = Column(Boolean)
    express_delivery = Column(Boolean)
    rating = Column(Float)
    categories = Column(ARRAY(String))
    attributes = Column(ARRAY(String))