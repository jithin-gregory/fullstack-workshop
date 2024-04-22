from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from fastapi import Depends

from app.dependency_injection import mongo_client
from database.MongoDBClient import MongoDBClient
from database.schemas.BaseDocument import BaseDocument

T = TypeVar('T', bound=BaseDocument)


class BaseCRUDRepository(Generic[T], ABC):

    def __init__(self, collection_name: str, db_client: MongoDBClient = Depends(mongo_client)):
        self.db_client = db_client
        self.collection_name = collection_name

    def insert(self, document: T):
        return self.db_client.insert_one(self.collection_name, document.model_dump(by_alias=True))

    def find_by_id(self, id):
        return self.db_client.find_one(self.collection_name, {"_id": id})

    def find(self, filter: dict) -> list[T]:
        documents = []
        for document in self.db_client.find_all(self.collection_name, filter):
            documents.append(self.map_to_document(document))
        return documents

    def update(self, filter: dict, document: T):
        return self.db_client.update_one(self.collection_name, filter, document.model_dump(by_alias=True))

    def delete(self, filter: dict):
        return self.db_client.delete_one(self.collection_name, filter)

    @abstractmethod
    def map_to_document(self, document: dict) -> T:
        pass
