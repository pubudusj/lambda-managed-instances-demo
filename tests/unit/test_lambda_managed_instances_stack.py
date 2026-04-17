import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_managed_instances.lambda_managed_instances_stack import LambdaManagedInstancesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_managed_instances/lambda_managed_instances_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaManagedInstancesStack(app, "lambda-managed-instances")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
