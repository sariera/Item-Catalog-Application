from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="im Robot", email="ar.rickxxx@gmail.com")
session.add(User1)
session.commit()

# Create category of Science Books
category1 = Categories(user_id=1, name="Science")
session.add(category1)
session.commit()


# Create category of Biography Books
category2 = Categories(user_id=1, name="Biographies")
session.add(category2)
session.commit()

# Create category of Romance Books
category3 = Categories(user_id=1, name="Romance")
session.add(category3)
session.commit()

# Create category of Fantasy Books
category4 = Categories(user_id=1, name="Fantasy")
session.add(category4)
session.commit()

# Create category of Art Books
category5 = Categories(user_id=1, name="Arts")
session.add(category5)
session.commit()

# Create category of Recipes Books
category6 = Categories(user_id=1, name="Recipes")
session.add(category6)
session.commit()

# Create category of Medicine Books
category7 = Categories(user_id=1, name="Medicine")
session.add(category7)
session.commit()

# Create category of History Books
category8 = Categories(user_id=1, name="History")
session.add(category8)
session.commit()

# Create category of Science Fiction Books
category9 = Categories(user_id=1, name="Science Fiction")
session.add(category9)
session.commit()

# Create category of Children Books
category10 = Categories(user_id=1, name="Children")
session.add(category10)
session.commit()

# Create category of Music Books
category11 = Categories(user_id=1, name="Music")
session.add(category11)
session.commit()