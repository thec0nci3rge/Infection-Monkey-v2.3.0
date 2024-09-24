---
title: "AWS Agent Launcher"
draft: false
description: "Run Infection Monkey on AWS EC2 instances"
tags: ["aws", "ec2", "ssm", "agent", "run"]
pre: "<i class='fa-brands fa-aws'></i> "
---

## Description

Infection Monkey enables you to launch Agents throughout your AWS
infrastructure without logging in to or modifying any of your EC2 instances.
Executing Infection Monkey on AWS EC2 instances is facilitated by the [AWS
Systems Manager (SSM) Agent](
https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html).
Each EC2 instance has an SSM Agent installed for updating, managing, and
configuring the instance. It executes requests received from the [AWS Systems
Manager](
https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html),
and uses the [Amazon Message Delivery Service](
https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmessagedeliveryservice.html)
to report status and execution details back to the Monkey Island.

In order to use this feature, your EC2 instances must meet the following
criteria:

1. The SSM Agent must be installed on the EC2 instance from which you will
   launch the Infection Monkey Agent.
1. The EC2 instance must have the necessary IAM roles to allow the SSM Agent to
   execute commands.


When the Monkey Island is deployed on any EC2 instance, (such as when using the
[Infection Monkey
AMI](https://aws.amazon.com/marketplace/pp/prodview-b3oqimxzrd762)), it will
automatically detect that it is running on within an AWS environment and the
option to launch Infection Monkey Agents on EC2 instances will become
available.

![Running Infection Monkey on EC2 Instances](
/images/island/integrations/aws/run_on_aws_ec2.png "Running Infection Monkey on EC2
Instances")
