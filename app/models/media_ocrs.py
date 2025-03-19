from sqlalchemy import Column, BigInteger, String, Text, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class MediaOCR(Base):
    __tablename__ = 'media_ocrs'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    media_id = Column(BigInteger, nullable=False)
    name = Column(String(191), nullable=True)
    ocr_raw = Column(Text, nullable=True)  # Using Text for mediumtext
    ocr_applied = Column(Text, nullable=True)  # Using Text for mediumtext
    ocr_applied_hash = Column(String(512), nullable=True)
    percentage = Column(Integer, default=0, nullable=False)
    folder_id = Column(BigInteger, default=0, nullable=False)
    folder_path = Column(String(2056), nullable=True)
    status = Column(Integer, default=0, nullable=False)
    meta = Column(Text, nullable=True)  # Using Text for mediumtext

    def __repr__(self):
        return f"<MediaOCR(id={self.id}, media_id={self.media_id}, name={self.name})>"