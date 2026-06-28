from app.database.database import Base
from app.database.database import engine
import app.models
print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)

print("Tables created successfully.")