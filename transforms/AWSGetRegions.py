import socket
from boto3.session import Session
from maltego_trx.maltego import UIM_TYPES
import maltego_trx.entities
from maltego_trx.entities import *
from maltego_trx.transform import DiscoverableTransform


class AWSGetRegions(DiscoverableTransform):
    """
    Receive DNS name from the client, and resolve to IP address.
    """

    @classmethod
    def create_entities(cls, request, response):
        for region in cls.get_regions():
            response.addEntity("sos.AWSRegion", region)
        
    @staticmethod
    def get_regions():
        regions = []
        session = Session()
        regions = session.get_available_regions('ec2')
        return regions


if __name__ == "__main__":
    print(AWSGetRegions.get_regions())

