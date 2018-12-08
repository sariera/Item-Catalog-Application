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


# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="Murder on Shades Mountain",
                             description="the legal lynching of Willie \
                               Peterson and the struggle for justice in \
                               Jim Crow Birmingham.",
                             categories=category8,
                             author="Melanie Morrison",
                             preview="https://covers.openlibrary.org/w/id/\
                             8202951-L.jpg")
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="A nervous state",
                             description="violence, remedies,\
                              and reverie in colonial Congo ",
                             categories=category7,
                             author="Nancy Rose Hunt",
                             preview="https://covers.openlibrary\
                             .org/w/id/8248353-L.jpg")
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Does a hippo go to the doctor?",
                             description="explores and explains why animals \
                             in the wild don't go to doctors",
                             categories=category10,
                             author="Harriet Ziefert",
                             preview="https://covers.openlibrary.org\
                             /w/id/8251993-L.jpg")
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Guile",
                             description="In the Bad Bayous, \
                             guile--a power in the water that \
                             changes people and objects, sometimes \
                             for the worse--sets Yonie Watereye, 16, \
                             on a path that puts her own life in danger \
                             as she traces her family tree and finds\
                             a murderer",
                             categories=category4,
                             author="Constance Cooper",
                             preview="https://covers.openlibrary.org/\
                             w/id/8223861-L.jpg")
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Peaceful Sundays",
                             description="The breakout first novel from \
                             author Jimmy Pete, Peaceful Sundays is a\
                             laugh-out-loud parody of American society",
                             categories=category3,
                             author="Jimmy Pete",
                             preview="https://covers.openlibrary.org\
                             /w/id/7898969-L.jpg")
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Making light",
                             description="Haydn, musical camp, \
                            and the long shadow of German idealism ",
                             categories=category11,
                             author="Raymond Knapp",
                             preview="https://covers.openlibrary.org\
                             /w/id/8133132-L.jpg")
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Posthumous images",
                             description="contemporary art and memory\
                                politics in post-civil war Lebanon ",
                             categories=category5,
                             author="Chad Elias",
                             preview="https://covers.openlibrary.org/\
                             w/id/8214195-L.jpg")
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Always hungry? ",
                             description="conquer cravings, retrain\
                            your fat cells, and lose weight perman\
                            ently",
                             categories=category6,
                             author="David Ludwig",
                             preview="https://covers.openlibrary.org/w\
                             /id/8113833-L.jpg")
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Future shock ",
                             description="Elena, nearly aged out of the\
                            foster care system, is recruited along with\
                            four other exceptional teens for a time-travel\
                            mission that will make them rich if they survive.",
                             categories=category9,
                             author="Elizabeth Briggs",
                             preview="https://covers.openlibrary.org\
                             /w/id/8199321-L.jpg")
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Humans Trails",
                             description="he central theme of\
                                the book is a conception of man\
                                and his behavior: How man differs\
                                from machine and whether there are\
                                some persons who are thought to be\
                                human beings but they are only\
                                human-like robots, mans imitatio\
                                ns.",
                             categories=category1,
                             author="Kyosti Waris",
                             preview="https://covers.openlibrary.org\
                             /b/id/8258750-L.jpg")
session.add(categoryItem1)
session.commit()

print "added category items!"
