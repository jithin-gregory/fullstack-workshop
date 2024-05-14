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

    def get_all_users(self):
        return list(self.db.users.find())

    def update_user_image_path(self, user_id, image_path):
        self.db.users.update_one(
            {"_id": ObjectId(user_id)}, {"$set": {"image_path": image_path}}
        )

    def get_user(self, user_id):
        return self.db.users.find_one({"_id": ObjectId(user_id)})

    def get_user_by_username(self, username: str):
        user_data = self.db.users.find_one({"username": username})
        if user_data:
            return UserDocument(**user_data)
        return None
