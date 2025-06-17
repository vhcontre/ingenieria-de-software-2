#file: backend/app/db/session.py
from sqlalchemy.orm import sessionmaker
from .engine import engine
from sqlalchemy.orm import Session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
