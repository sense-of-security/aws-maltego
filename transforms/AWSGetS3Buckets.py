import socket
import boto3  
from boto3.session import Session
from maltego_trx.maltego import UIM_TYPES
import maltego_trx.entities
from maltego_trx.entities import *
from maltego_trx.transform import DiscoverableTransform


class AWSGetS3Buckets(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):
        s3 = boto3.resource('s3', region_name=request.Value)
        for bucket in s3.buckets.all():
            entity = response.addEntity("sos.AWSS3Bucket", bucket)
            entity.addProperty("RegionName", "Region Name", "strict", request.Value)  


if __name__ == "__main__":
    print("Nothing to see here")
