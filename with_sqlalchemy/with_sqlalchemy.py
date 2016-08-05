from contextlib import contextmanager

from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


@contextmanager
def session_scope():
    # __init__
    engine = create_engine("sqlite:///test.db")
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # __enter__
    try:
        yield Session()
    # __exit__
        session.commit()
    except Exception as e:
        session.rollback()
        # raise e
    else:
        print('No problem detected')
    finally:
        print('Session closed')
        session.close()


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

with session_scope() as session:
    ed_user = User(id=1000, name='ed', fullname='Ed Jones', password='edspassword')
    ed_user2 = User(id=1000, name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
from sqlalchemy import inspect
insp = inspect(ed_user)
print(insp.session)
