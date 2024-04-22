from fastapi import Depends

from app.dependency_injection import mongo_client
from database.MongoDBClient import MongoDBClient
from database.schemas import UserDocument
from utils.contants import db_constants
from .BaseCRUDRepository import BaseCRUDRepository


class UserRepository(BaseCRUDRepository[UserDocument]):

    def __init__(self, db_client: MongoDBClient = Depends(mongo_client)):
        super().__init__(db_constants.USER_COLLECTION, db_client)

    def map_to_document(self, user: dict) -> UserDocument:
        return UserDocument(id=user['_id'],
                            email=user['email'],
                            username=user['username'],
                            first_name=user['first_name'],
                            last_name=user['last_name'],
                            user_role=user['user_role'],
                            password=user['password'])
