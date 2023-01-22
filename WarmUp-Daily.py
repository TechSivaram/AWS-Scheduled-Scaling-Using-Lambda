import boto3

region = "us-east-x"
asc = boto3.client("autoscaling", region_name=region)
alb = boto3.client("elbv2", region_name=region)


def lambda_handler(event, context):
    response = asc.start_instance_refresh(
        AutoScalingGroupName="xyz-groupName",
        Strategy="Rolling",
        DesiredConfiguration={
            "MixedInstancesPolicy": {
                "LaunchTemplate": {"Overrides": [{"InstanceType": "c6in.4xlarge"}]}
            }
        },
    )

    response = alb.modify_rule(
        RuleArn="arn:aws:elasticloadbalancing:us-east-x:account:listener-rule/app/xyzalb/xxxxxx/xxxxxxx/xxxxxxxxxxx",
        Actions=[
            {
                "Type": "forward",
                "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-x:account:targetgroup/xyzgroup/xxxxxxxxxxxx",
            }
        ],
    )

    response = alb.modify_rule(
        RuleArn="arn:aws:elasticloadbalancing:us-east-x:account:listener-rule/app/xyzalb/xxxxxxx/xxxxx/xxxxxxxxxxxxxxxxx",
        Actions=[
            {
                "Type": "forward",
                "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-x:account:listener:targetgroup/abcgroup/xxxxxxxxxxxxxxxxxx",
            }
        ],
    )
