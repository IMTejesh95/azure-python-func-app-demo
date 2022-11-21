import logging

import azure.functions as func
from azure.cosmos import CosmosClient
from os import environ
from uuid import uuid4
import json

cosmos = CosmosClient(environ['DB_URI'], credential=environ['DB_RO_KEY'])
DB_NAME = environ['DB_NAME'] or 'demo-app-db'


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Add new book record.
    """
    print("Creating new book record...")
    try:
        req_body = req.get_json()

        db = cosmos.get_database_client(DB_NAME)
        books_container = db.get_container_client('books')

        added_book = books_container.create_item({
            "id": str(uuid4()),
            "name": req_body['title'],
            "author": req_body['author']
        })
        return func.HttpResponse(
            json.dumps(added_book),
            status_code=201
        )
    except Exception as e:
        logging.exception(e)
        return func.HttpResponse(
            "Something went wrong!",
            status_code=500
        )
