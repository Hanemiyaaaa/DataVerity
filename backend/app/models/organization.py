from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    registration_number = Column(String, unique=True, index=True)

    country = Column(String)