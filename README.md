# AWS-Scheduled-Scaling-Using-Lambda
AWS - Scheduled Scaling Using Lambda

Using Path based routing in one of my environment

But the traffic on this web api is less at night.

Seen a cost savings opportunity here by changing instance type and scale dow.

But we need to refresh the instances and warm up the environment by scaling to desired capacity and instance type.

This is a lambda code which will be triggered from eventBridge, which do trigger on schedule.

But it needs all required permissoions. 

![image](https://user-images.githubusercontent.com/85802871/213940706-3a28e447-af37-4ea5-a0c6-16f1eda4c3ea.png)
