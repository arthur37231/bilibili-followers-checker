from flask import request


# Extract request params from Flask request
def get_request_params():
    params = request.get_json()

    if params is None:
        params = request.form.to_dict()

    query_params = {
        k: v
        for k, v in request.args.items()
    }
    params = {**params, **query_params}
    return params
