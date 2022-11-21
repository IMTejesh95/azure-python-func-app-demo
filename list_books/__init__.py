import logging

import azure.functions as func
from azure.cosmos import CosmosClient
from os import environ
import json

cosmos = CosmosClient(environ['DB_URI'], credential=environ['DB_RO_KEY'])
DB_NAME = environ['DB_NAME'] or 'demo-app-db'


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    List all the books from container.
    """
    try:
        db = cosmos.get_database_client(DB_NAME)
        books_container = db.get_container_client('books')

        books = books_container.read_all_items()

        return func.HttpResponse(
            json.dumps(list(books)),
            status_code=200
        )
    except Exception as e:
        logging.exception(e)
        return func.HttpResponse(
            "Something went wrong!",
            status_code=500
        )
