from app.database.database import Base
from app.models import Course

print("Registered Tables:")
print(Base.metadata.tables.keys())