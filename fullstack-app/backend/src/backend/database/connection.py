from sqlmodel import create_engine, Session

# URL koneksi pake port 5433 sesuai sama docker-compose
DATABASE_URL = "postgresql://postgres:1234@localhost:5433/acara-rsi"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session