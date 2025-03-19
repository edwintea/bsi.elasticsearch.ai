from sqlalchemy import Column, BigInteger, String, Integer, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartImages(Base):
    __tablename__ = 'part_images'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(191), nullable=True, index=True)
    vehicle_id = Column(BigInteger, nullable=True, index=True)
    part_id = Column(BigInteger, nullable=True, index=True)
    image = Column(BigInteger, nullable=True, index=True)
    media_ocr_id = Column(BigInteger, nullable=True, index=True)
    spatie_image_id = Column(BigInteger, nullable=True, index=True)
    percentage = Column(Integer, nullable=True)
    status_api = Column(Integer, default=0, nullable=True, index=True)
    status = Column(Integer, default=0, nullable=True, index=True)
    meta = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return (f"<PartImages(id={self.id}, name={self.name}, vehicle_id={self.vehicle_id}, "
                f"part_id={self.part_id}, status={self.status})>")