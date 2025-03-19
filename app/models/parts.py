from sqlalchemy import Column, BigInteger, String, Text, Integer, TIMESTAMP, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Parts(Base):
    __tablename__ = 'parts'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), nullable=True, index=True)
    name = Column(String(191), nullable=True, index=True)
    part_group_id = Column(BigInteger, nullable=True, index=True)
    part_category_id = Column(BigInteger, nullable=True, index=True)
    image = Column(BigInteger, nullable=True)
    description = Column(Text, nullable=True)
    status = Column(Integer, default=0, nullable=True)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    published_at = Column(DateTime, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return (f"<Parts(id={self.id}, code={self.code}, name={self.name}, "
                f"part_group_id={self.part_group_id}, part_category_id={self.part_category_id})>")