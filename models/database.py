from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Для простоты используем SQLite

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class OwnerDB(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    fio = Column(String, index=True)
    date_birth = Column(String)
    region = Column(String)
    passport = Column(String, unique=True, index=True)
    inn = Column(String, unique=True, index=True)

    cars = relationship("CarDB", back_populates="owner")


class CarDB(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    VIN = Column(String, index=True)
    gos_number = Column(String)
    owner_id = Column(Integer, ForeignKey('owners.id'))

    owner = relationship("OwnerDB", back_populates="cars")


Base.metadata.create_all(bind=engine)