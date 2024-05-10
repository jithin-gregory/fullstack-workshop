from pymongo import MongoClient
from bson import ObjectId
from document.user_document import UserDocument


class UserRepository:
    def __init__(self):
        client = MongoClient("mongodb://localhost:27017")
        self.db = client["user_db"]

    def create_user(self, user: UserDocument):
        result = self.db.users.insert_one(user.model_dump())
        return str(result.inserted_id)
