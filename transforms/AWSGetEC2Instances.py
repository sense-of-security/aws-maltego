import socket
import boto3  
from boto3.session import Session
from maltego_trx.maltego import UIM_TYPES
import maltego_trx.entities
from maltego_trx.entities import *
from maltego_trx.transform import DiscoverableTransform


class AWSGetEC2Instances(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):
        client = boto3.client('ec2', region_name=request.Value)
        r = client.describe_instances()
        for reservation in r["Reservations"]:
            for instance in reservation["Instances"]:
                entity = response.addEntity("sos.AWSEC2Instance", instance['InstanceId'])
                entity.addDisplayInformation(title=f"{instance['InstanceId']} ({instance['KeyName']})")
                entity.addProperty("InstanceType", "Instance Type", "strict", instance["InstanceType"])
                entity.addProperty("KeyName", "Key Name", instance["KeyName"])
                entity.addProperty("PrivateIp", "Private Ip", "strict", instance["PrivateIpAddress"])
                entity.addProperty("RegionName", "Region Name", "strict", request.Value)  


if __name__ == "__main__":
    print("Nothing to see here")

