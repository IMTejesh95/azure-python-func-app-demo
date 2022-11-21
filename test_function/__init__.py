import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    edu = req.route_params.get('edu')
    name = req.params.get('name')
    try:
        req_body = req.get_json()
        lastname = req_body.get('lastname')
    except ValueError:
        pass

    if name:
        return func.HttpResponse(f"Hello, {name} {lastname} ({edu}). This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
