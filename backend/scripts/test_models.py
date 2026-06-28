from app.database.database import Base
import app.models
 
print("Registered Tables:")
print(Base.metadata.tables.keys())