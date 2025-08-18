import json
import logging
import os
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
# from utils import respond #package-style import
from utils.response import respond #Absolute import

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lamda_handler(event, context):
    logger.info(f'event: {json.dumps(event)}')
    result = {"message": "Hello from get.py!"}
    return respond(None, result)

    
