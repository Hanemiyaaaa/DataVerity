from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)

    organization_id = Column(Integer, ForeignKey("organizations.id"))

    coefficient_id = Column(Integer, ForeignKey("coefficients.id"))

    value = Column(Float)

    organization = relationship("Organization")

    coefficient = relationship("Coefficient")