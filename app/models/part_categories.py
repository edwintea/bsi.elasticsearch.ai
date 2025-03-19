from sqlalchemy import Column, BigInteger, String, Text, Double, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartCategory(Base):
    __tablename__ = 'part_categories'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(191), nullable=True)
    image = Column(BigInteger, nullable=True)
    description = Column(Text, nullable=True)
    x = Column(Double(8, 2), nullable=True)
    y = Column(Double(8, 2), nullable=True)
    status = Column(Integer, default=0, nullable=True)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return f"<PartCategory(id={self.id}, name={self.name}, status={self.status})>"