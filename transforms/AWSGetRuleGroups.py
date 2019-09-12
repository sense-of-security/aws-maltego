import socket
from maltego_trx.maltego import UIM_TYPES
import maltego_trx.entities
from maltego_trx.entities import *
from maltego_trx.transform import DiscoverableTransform


class AWSGetRuleGroups(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):
        region = request.Properties["RegionName"]
        groupid = request.Properties["GroupId"]
        
        entity = response.addEntity("sos.AWSInboundRule", "Inbound Rules")
        entity.addDisplayInformation("Inbound Rules")
        entity.addProperty("GroupId", "Group Id", "strict", groupid)
        entity.addProperty("RegionName", "Region Name", "strict", region)

        entity = response.addEntity("sos.AWSOutboundRule", "Outbound Rules")
        entity.addDisplayInformation("Outbound Rules")
        entity.addProperty("GroupId", "Group Id", "strict", groupid)
        entity.addProperty("RegionName", "Region Name", "strict", region)


if __name__ == "__main__":
    print("Nothing to see here")

