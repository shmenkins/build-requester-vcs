import boto3
import json
import logging
import os
import uuid
from shmenkins import logging, aws

logger = logging.get_logger()

topic_artifact_outdated = aws.Topic("artifact_outdated")


def handler(event, context):
    logger.debug("Handling %s", str(event))

    # parse input
    body = json.loads(event["body"])
    url = body["repository"]["url"]
    interaction_id = str(uuid.uuid4())

    # publish event
    publish_event({"interaction_id": interaction_id, "url": url})

    logger.debug("Finished handling %s", str(event))

    return {"statusCode": "201", "headers": {"X-Shmenkins-InteractionId": interaction_id}}


def publish_event(obj):
    topic_artifact_outdated.publish(obj)
