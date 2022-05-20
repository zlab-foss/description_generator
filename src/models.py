import uuid

from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY, UUID

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
    
    log = relationship("Log", back_populates="product")



class Log(Base):
    __tablename__ = "log"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    product_id = Column(Integer, ForeignKey("product.id"))
    time_stamp = Column(DateTime, default=datetime.utcnow())

    product = relationship("Product", back_populates="log")