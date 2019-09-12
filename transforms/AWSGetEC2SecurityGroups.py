import socket
import boto3  
from boto3.session import Session
from maltego_trx.maltego import UIM_TYPES
import maltego_trx.entities
from maltego_trx.entities import *
from maltego_trx.transform import DiscoverableTransform


class AWSGetEC2SecurityGroups(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):
        region = request.Properties["RegionName"]
        instanceid = request.Value
        ec2 = boto3.resource('ec2', region)
        instances = ec2.instances.filter(
            Filters=[{
                'Name': 'instance-id',
                'Values': [instanceid]
                }]
            )
        for instance in instances:
            for sg in instance.security_groups:
                entity = response.addEntity("sos.AWSSecurityGroup", sg['GroupName'])
                entity.addProperty("GroupId", "Group Id", "loose", sg['GroupId'])
                entity.addProperty("RegionName", "Region Name", "loose",request.Properties["RegionName"])


if __name__ == "__main__":
    print("Nothing to see here")

