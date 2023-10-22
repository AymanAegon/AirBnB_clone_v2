#!/usr/bin/python3
"""
new database srorage systeme
"""
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """ DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """
        defintition of env variables
        """
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}",
            pool_pre_ping=True,
        )

        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session
        """
        allClasses = [User, State, Place, Amenity, City, Review]
        result = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                ClassName = obj.__class__.__name__
                kn = ClassName + "." + obj.id
                result[kn] = obj
        else:
            for clss in allClasses:
                for obj in self.__session.query(clss).all():
                    ClassName = obj.__class__.__name__
                    kn = ClassName + "." + obj.id
                    result[kn] = obj
        return result

    def reload(self):
        """ the reload function """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def new(self, obj):
        """add a new object"""
        if obj:
            self.__session.add(obj)

    def delete(self, obj=None):
        """delete objects from the database"""
        if obj:
            self.__session.delete(obj)

    def save(self):
        """saves the changes"""
        self.__session.commit()

    def close(self):
        """close method"""
        self.__session.close()
