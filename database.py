from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#DATABASE_URL = "mysql+mysqlconnector:////admin:cyberia3@database-2.cqc0gyrlhuoi.us-east-1.rds.amazonaws.com/teste_ba?charset=utf8mb4"
DATABASE_URL="mysql+pymysql://admin:cyberia3@database-2.cqc0gyrlhuoi.us-east-1.rds.amazonaws.com/teste_ba?charset=utf8mb4"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
