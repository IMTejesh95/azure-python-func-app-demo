import logging

import azure.functions as func
from azure.cosmos import CosmosClient, exceptions, PartitionKey
from os import environ
from uuid import uuid4


cosmos = CosmosClient(environ['DB_URI'], credential=environ['DB_RO_KEY'])
DB_NAME = environ['DB_NAME'] or 'demo-app-db'


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Create and initialize databsae with some dummy data.
    """
    logging.info(environ)
    req_body = req.get_json()
    try:
        logging.info('Initializing database...')
        try:
            db = cosmos.create_database(DB_NAME)
        except exceptions.CosmosResourceExistsError:
            db = cosmos.get_database_client(DB_NAME)
            logging.info(f"Database already exists with id {DB_NAME}")

        try:
            container = db.create_container(
                'books', partition_key=PartitionKey(path="/name"))
        except exceptions.CosmosResourceExistsError:
            container = db.get_container_client('books')
            logging.info(f"Container exists with id books")

        # Insert documents in container
        if req_body:
            container.create_item(
                {
                    "id": str(uuid4()),
                    "name": req_body['title'],
                    "author": req_body['author']
                })

        return func.HttpResponse(
            "Database initialized successfully.",
            status_code=200)
    except Exception as e:
        logging.exception(e)
        return func.HttpResponse(
            e.message,
            status_code=500
        )
