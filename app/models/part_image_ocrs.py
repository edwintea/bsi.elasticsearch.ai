from sqlalchemy import Column, BigInteger, String, Text, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartImageOCRs(Base):
    __tablename__ = 'part_image_ocrs'

    my_row_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    id = Column(String(36), nullable=False, index=True)  # Using String for CHAR(36)
    code = Column(String(50), nullable=True, index=True)
    text_ori = Column(String(191), nullable=True)
    ocr_pos_hash = Column(String(191), nullable=True, index=True)
    vehicle_id = Column(BigInteger, nullable=True, index=True)
    part_id = Column(BigInteger, nullable=True, index=True)
    part_image_id = Column(BigInteger, nullable=True, index=True)
    coordinate = Column(Text, nullable=True)
    status = Column(Integer, default=0, nullable=True, index=True)
    meta = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    status_api = Column(Integer, default=0, nullable=True)

    def __repr__(self):
        return (f"<PartImageOCRs(my_row_id={self.my_row_id}, id={self.id}, "
                f"code={self.code}, text_ori={self.text_ori}, "
                f"vehicle_id={self.vehicle_id}, part_id={self.part_id})>")