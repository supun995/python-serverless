import json

def respond(err, result=None):
    body = {}
    if err:
        body = json.dumps({'error' : err})
    else:
        body = json.dumps(result)

    return {
        'statusCode' : '400' if err else '200',
        'body' : body,
        'headers' : {
            'Content-Type' : 'application/json',
            'Access-Control-Allow-Origin' : '*'
        }
    }