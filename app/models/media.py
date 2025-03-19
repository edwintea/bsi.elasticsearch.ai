from sqlalchemy import Column, BigInteger, String, CHAR, Text, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Media(Base):
    __tablename__ = 'media'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)  # Removed unsigned
    model_type = Column(String(191), nullable=False)
    model_id = Column(BigInteger, nullable=False)  # Removed unsigned
    uuid = Column(CHAR(36), unique=True, nullable=True)
    collection_name = Column(String(191), nullable=False)
    name = Column(String(191), nullable=False)
    file_name = Column(String(191), nullable=False)
    mime_type = Column(String(191), nullable=True)
    disk = Column(String(191), nullable=False)
    conversions_disk = Column(String(191), nullable=True)
    size = Column(BigInteger, nullable=False)  # Removed unsigned
    manipulations = Column(Text, nullable=False)
    custom_properties = Column(Text, nullable=False)
    generated_conversions = Column(Text, nullable=False)
    responsive_images = Column(Text, nullable=False)
    order_column = Column(Integer, nullable=True)  # Removed unsigned
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<Media(id={self.id}, name={self.name}, model_type={self.model_type})>"