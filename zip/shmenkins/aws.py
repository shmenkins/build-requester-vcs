import boto3
import json

_region = boto3.session.Session().region_name
_account = boto3.client("sts").get_caller_identity().get("Account")
_sns = boto3.resource("sns")

class Topic:
    def __init__(self, topic_name: str) -> None:
        self.__topic = _sns.Topic("arn:aws:sns:" + _region + ":" + _account + ":" + topic_name)


    def publish(self, msg: dict) -> None:
        """ Publish a message, msg must be dict and is converted to json """
        self.__topic.publish(Message=json.dumps(msg))
