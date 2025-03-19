from sqlalchemy import Column, BigInteger, String, Text, Integer, TIMESTAMP, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    title = Column(String(191), nullable=True)
    slug = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)  # Using Text for longtext
    image = Column(BigInteger, nullable=True)
    model = Column(String(191), nullable=True)
    status = Column(Integer, default=0, nullable=True)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    published_at = Column(DateTime, nullable=True)
    category_description = Column(String(191), nullable=False, default="Light Duty")
    emission = Column(String(191), nullable=False, default="EURO 2")

    def __repr__(self):
        return (f"<Vehicles(id={self.id}, title={self.title}, slug={self.slug}, "
                f"model={self.model}, status={self.status})>")