from fastapi import Depends
from typing import TypeVar

from app.dependency_injection import mongo_client
from database.MongoDBClient import MongoDBClient
from database.schemas.BaseDocument import BaseDocument


class BaseCRUDRepository:
    T = TypeVar('T', bound=BaseDocument)

    def __init__(self, collection_name: str, db_client: MongoDBClient = Depends(mongo_client)):
        self.db_client = db_client
        self.collection_name = collection_name

    def insert(self, document: T):
        return self.db_client.insert_one(self.collection_name, document.model_dump(by_alias=True))

    async def find_by_id(self, id):
        return await self.db_client.find_one(self.collection_name, {"_id": id})

    async def find(self, filter: dict):
        return await self.db_client.find_all(self.collection_name, filter)

    async def update(self, filter: dict, document: T):
        return await self.db_client.update_one(self.collection_name, filter, document.model_dump(by_alias=True))

    async def delete(self, filter: dict):
        return await self.db_client.delete_one(self.collection_name, filter)
