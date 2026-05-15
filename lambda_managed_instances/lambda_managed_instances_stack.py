import os

from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_lambda as lambda_,
)
from constructs import Construct
from dotenv import load_dotenv

load_dotenv()


class LambdaManagedInstancesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc_id = os.environ["VPC_ID"]
        subnet_ids = [s.strip() for s in os.environ["SUBNET_IDS"].split(",")]

        # Look up existing VPC
        vpc = ec2.Vpc.from_lookup(self, "Vpc", vpc_id=vpc_id)

        # Look up existing subnets
        subnets = [
            ec2.Subnet.from_subnet_id(self, f"Subnet{i}", subnet_id)
            for i, subnet_id in enumerate(subnet_ids)
        ]

        # Security group for the capacity provider
        security_group = ec2.SecurityGroup(
            self,
            "CapacityProviderSG",
            vpc=vpc,
            description="Security group for Lambda capacity provider",
        )

        # Create the Lambda capacity provider (managed instances)
        capacity_provider = lambda_.CapacityProvider(
            self,
            "CapacityProvider",
            subnets=subnets,
            security_groups=[security_group],
        )

        # Create the Lambda function
        fn = lambda_.Function(
            self,
            "ManagedInstanceFunction",
            runtime=lambda_.Runtime.PYTHON_3_14,
            handler="handler.handler",
            code=lambda_.Code.from_asset("lambda"),
        )

        # Attach the function to the capacity provider
        capacity_provider.add_function(fn)
