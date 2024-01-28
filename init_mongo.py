import pandas as pd
from pymongo import MongoClient
import settings

try:
    df = pd.read_csv(settings.INIT_FILE_PATH)
    try:
        client = MongoClient(settings.MONGODB_URL)
        db = client[settings.DATABASE_NAME]
        collection = db[settings.APP_COL]
    except Exception as db_error:
        print("Error connecting to the database:", db_error)
        raise db_error

    schema = df.columns.tolist()

    for _, row in df.iterrows():
        document = {}
        for field in schema:
            document[field] = row[field]
        document['_id'] = int(row['adId'])
        collection.insert_one(document)

    print("Data inserted into MongoDB.")

except FileNotFoundError as file_error:
    print("File not found:", file_error)

except Exception as e:
    print("An error occurred:", e)
