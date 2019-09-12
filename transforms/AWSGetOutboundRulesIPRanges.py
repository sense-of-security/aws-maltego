import socket
import boto3  
from boto3.session import Session
from maltego_trx.maltego import UIM_TYPES
import maltego_trx.entities
from maltego_trx.entities import *
from maltego_trx.transform import DiscoverableTransform


class AWSGetOutboundRulesIPRanges(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):
        rulesString = request.Value
        region = request.Properties["RegionName"]
        groupid = request.Properties["GroupId"]
        ec2 = boto3.resource('ec2', region)
        groups = ec2.security_groups.filter(
            Filters=[{
                'Name': 'group-id',
                'Values': [groupid]
                }]
            )
        
        for group in groups:
            for rule in group.ip_permissions_egress:
                if rule['IpProtocol'] == '-1':
                    rule['IpProtocol'] = 'ALL'
                if 'FromPort' not in rule:
                    rule['FromPort'] = 'ANY'
                if 'ToPort' not in rule:
                    rule['ToPort'] = 'ANY'
                label = f"{rule['IpProtocol']}:{rule['FromPort']}-{rule['ToPort']}"
                if rulesString == label:
                    for iprange in rule['IpRanges']:
                        entity = response.addEntity("sos.AWSEgressRange", iprange['CidrIp'])
                        entity.addProperty("GroupId", "Group Id", groupid)
                        entity.addProperty("RegionName", "Region Name","strict", region)

if __name__ == "__main__":
    print("Nothing to see here")