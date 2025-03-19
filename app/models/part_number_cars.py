from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartNumberCars(Base):
    __tablename__ = 'part_number_cars'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), nullable=True, index=True)
    part_number = Column(String(191), nullable=True)
    stock = Column(BigInteger, default=0, nullable=False)
    price = Column(BigInteger, default=0, nullable=False)
    product_category_id = Column(BigInteger, nullable=True)
    product_type = Column(String(191), nullable=True)
    name = Column(String(191), nullable=True)
    description = Column(Text, nullable=True)
    remarks = Column(Text, nullable=True)
    colour = Column(String(191), nullable=True)
    is_warranty = Column(Integer, default=0, nullable=False)  # Using Integer for tinyint
    reference_code = Column(String(191), nullable=True)
    year = Column(String(191), nullable=True)
    part_label = Column(String(191), nullable=True)
    alternatif_part_number = Column(String(191), nullable=True)
    model_code = Column(String(191), nullable=True)
    supplier_code = Column(String(191), nullable=True)
    alternatif_part_name = Column(String(191), nullable=True)
    is_manually_input = Column(Integer, default=0, nullable=True)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    updated_stock_at = Column(DateTime, nullable=True)
    api_last_checked = Column(DateTime, nullable=True)
    api_last_modified_value = Column(DateTime, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return (f"<PartNumberCars(id={self.id}, code={self.code}, part_number={self.part_number}, "
                f"stock={self.stock}, price={self.price}, name={self.name})>")