from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Coefficient(Base):
    __tablename__ = "coefficients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True)

    formula = Column(String)