from sqlalchemy import Column, BigInteger, String, Text, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartGroup(Base):
    __tablename__ = 'part_groups'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    code = Column(String(10), unique=True, nullable=True)
    name = Column(String(191), nullable=True)
    part_category_id = Column(BigInteger, nullable=True)
    image = Column(BigInteger, nullable=True)
    description = Column(Text, nullable=True)
    status = Column(Integer, default=0, nullable=True)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return f"<PartGroup(id={self.id}, code={self.code}, name={self.name})>"