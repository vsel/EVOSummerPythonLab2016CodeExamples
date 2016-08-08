from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password
        )

engine = create_engine("sqlite:///test.db")
# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
ed_user = User(id=1, name='ed', fullname='Ed Jones', password='edspassword')
ed_user2 = User(id=2, name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)
session.add(ed_user2)
session.commit()

