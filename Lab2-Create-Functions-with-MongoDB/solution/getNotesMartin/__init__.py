import logging
import pymongo
from bson.json_util import dumps
import os

import azure.functions as func
logging.info('getNotesMartin function processed a request.')


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        url = os.environ["MyDbConnection"] # Change the Variable name, as applicable to you
        logging.info(f'Connection URL: {url}')
        client = pymongo.MongoClient(url)
        database = client['course2db'] # Change the MongoDB name
        collection = database['sampleCollection']    # Change the collection name
        logging.info('Successfully connected to MongoDB')
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except ConnectionError:
        logging.error("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)