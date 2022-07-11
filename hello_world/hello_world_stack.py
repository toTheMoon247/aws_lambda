from cgitb import handler
from typing_extensions import runtime
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _aws_lambda_event_sources,
)

# import os.path
# dirname = os.path.dirname(__file__)


class HelloWorldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "HelloWorldQueue",
            visibility_timeout=Duration.seconds(300),
        )

        sqs_lambda = _lambda.Function(self, 'SQSLambdaTrigger',
            handler='lambda_handler.handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('/Users/samchaim/Code/aws/hello_world/lambda')
        )

        sqs_event_source = _aws_lambda_event_sources.SqsEventSource(queue)
        sqs_lambda.add_event_source(sqs_event_source)

        topic = sns.Topic(
            self, "HelloWorldTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
