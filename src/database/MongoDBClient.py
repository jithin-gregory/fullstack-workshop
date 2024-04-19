from pymongo import MongoClient


class MongoDBClient:
    """
    Client class for interacting with a MongoDB database.

    Attributes:
        client (MongoClient): The MongoClient instance for connecting to the database.
        database_name (str): The name of the database to use.
    """

    def __init__(self, uri: str, database_name: str):
        """
        Initializes a MongoDBClient instance.

        Args:
            uri (str): The MongoDB connection URI.
            database_name (str): The name of the database to use.
        """

        self.client = MongoClient(uri)
        self.database_name = database_name

    def get_instance(self, uri: str = None, database_name: str = None):
        """
        Returns the existing MongoClient instance or creates a new one if not found.

        Args:
            uri (str): The MongoDB connection URI.
            database_name (str): The name of the database to use.
        """

        if self.client is None:
            self.client = MongoClient(uri)
            self.database_name = database_name
        return self


    def get_database(self):
        """
        Returns the database object for the specified database name.

        Returns:
            Database: The database object from the MongoClient instance.
        """

        return self.client[self.database_name]

    def insert_one(self, collection_name: str, document: dict):
        """
        Inserts a single document into a collection.

        Args:
            collection_name (str): The name of the collection to insert into.
            document (dict): The document to insert.

        Returns:
            ObjectId: The ID of the inserted document.
        """

        database = self.get_database()
        collection = database[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    async def find_one(self, collection_name: str, filter: dict = None):
        """
        Finds one document in a collection that matches the given filter.

        Args:
            collection_name (str): The name of the collection to search in.
            filter (dict, optional): A dictionary representing the filter criteria. Defaults to None.

        Returns:
            dict: The first document that matches the filter, or None if not found.
        """

        database = self.get_database()
        collection = database[collection_name]
        return await collection.find_one(filter)

    def find_all(self, collection_name: str, filter: dict = None):
        """
        Finds all documents in a collection that match the given filter.

        Args:
            collection_name (str): The name of the collection to search in.
            filter (dict, optional): A dictionary representing the filter criteria. Defaults to None.

        Returns:
            Cursor: A Cursor object containing the found documents.
        """

        database = self.get_database()
        collection = database[collection_name]
        return collection.find(filter, sort=None)  # You can add sorting options here

    def update_one(self, collection_name: str, filter: dict, update_document: dict):
        """
        Updates one document in a collection that matches the given filter.

        Args:
            collection_name (str): The name of the collection to update in.
            filter (dict): A dictionary representing the filter criteria.
            update_document (dict): A dictionary representing the update operations.

        Returns:
            UpdateResult: The update result object.
        """

        database = self.get_database()
        collection = database[collection_name]
        return collection.update_one(filter, update_document)

    def delete_one(self, collection_name: str, filter: dict):
        """
        Deletes one document in a collection that matches the given filter.

        Args:
            collection_name (str): The name of the collection to delete from.
            filter (dict): A dictionary representing the filter criteria.

        Returns:
            DeleteResult: The delete result object.
        """

        database = self.get_database()
        collection = database[collection_name]
        return collection.delete_one(filter)
