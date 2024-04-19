from fastapi import Depends

from app.dependency_injection import mongo_client
from database.MongoDBClient import MongoDBClient
from database.schemas import UserDocument
from utils.contants import db_constants
from .BaseCRUDRepository import BaseCRUDRepository


class UserRepository(BaseCRUDRepository):

    def __init__(self, db_client: MongoDBClient = Depends(mongo_client)):
        super().__init__(db_constants.USER_COLLECTION, db_client)
