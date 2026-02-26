import pymongo
from bson.binary import Binary
import os
from dotenv import load_dotenv

load_dotenv()

class MongoDBHandler:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION"))
            self.db = self.client[os.getenv("MONGODB_DATABASE")]
            self.collection = self.db[os.getenv("MONGODB_COLLECTION")]

            print("Connected to MongoDB successfully.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    ## Method to store file data, query, and analysis result in MongoDB
    def store_data(self, file_path: str, query: str, analysis_result:str):
        with open(file_path, "rb") as f:
            binary_data = f.read()

        file_document = {
            "filename": os.path.basename(file_path),
            "file_type": "application/pdf",
            "data": Binary(binary_data, subtype=0),
            "query": query,
            "analysis_result": analysis_result
        }

        self.collection.insert_one(file_document)
        print(f"File '{file_path}' stored successfully in MongoDB.")

if __name__ == "__main__":
    mongo_handler = MongoDBHandler()
    mongo_handler.store_data("data/sample.pdf", "What is the total revenue?", "The total revenue is $10 million.")