#!/usr/bin/env python3
import os

from dotenv import load_dotenv

load_dotenv()

import aws_cdk as cdk

from lambda_managed_instances.lambda_managed_instances_stack import (
    LambdaManagedInstancesStack,
)


app = cdk.App()
LambdaManagedInstancesStack(
    app,
    "LambdaManagedInstancesStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION"),
    ),
)

app.synth()
