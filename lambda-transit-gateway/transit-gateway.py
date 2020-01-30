import boto3
import time
import sys

#create transit gateway
def create_transit_gateway():
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway(
        Description='string',
        Options={
            'AmazonSideAsn': 64512,
            'AutoAcceptSharedAttachments': 'disable',
            'DefaultRouteTableAssociation': 'disable',
            'DefaultRouteTablePropagation': 'disable',
            'VpnEcmpSupport': 'enable',
            'DnsSupport': 'enable',
            'MulticastSupport': 'enable'
        },
        TagSpecifications=[
            {
                'ResourceType':'transit-gateway',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'aquis-terraform-boto3-tgw'
                    },
                ]
            },
        ],
        DryRun=False

    )
    return response

#create transit gateway VPC attachment
def create_transit_gateway_vpc_attachment(transit_gateway_id, vpc_id, subnet_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_vpc_attachment(
        TransitGatewayId=transit_gateway_id,
        VpcId=vpc_id,
        SubnetIds=[
            subnet_id,
        ],
        Options={
            'DnsSupport': 'enable',
            'Ipv6Support': 'disable'
        },
        TagSpecifications=[
            {
                'ResourceType': 'transit-gateway-attachment',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'aquis-terraform-boto3-tgw-attachment'
                    },
                ]
            },
        ],
        DryRun=False
    )
    return response

#Create transit gateway route-table
def create_transit_gateway_rt(transit_gateway_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_route_table(
        TransitGatewayId=transit_gateway_id,
        TagSpecifications=[
            {
                'ResourceType': 'transit-gateway-route-table',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'aquis-terraform-boto3-tgw-rtable'
                    },
                ]
            },
        ],
        DryRun=False
    )
    return response

#Create transit gateway route
def create_transit_gateway_route(transit_gateway_rt_id, destination_ip_block, transit_gateway_attachment_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_route(
        DestinationCidrBlock=destination_ip_block,
        TransitGatewayRouteTableId=transit_gateway_rt_id,
        TransitGatewayAttachmentId=transit_gateway_attachment_id,
        Blackhole=False,
        DryRun=False
    )
    return response

#Associate transit gateway route table
def associate_transit_gateway_route_table(tgw_rt_id, tgw_attach_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.associate_transit_gateway_route_table(
        TransitGatewayRouteTableId=tgw_rt_id,
        TransitGatewayAttachmentId=tgw_attach_id,
        DryRun=False
    )
    return response

#Enable transit gateway route table propogation
def enable_transit_gateway_route_table_propagation(tgw_rt_id, tgw_att_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.enable_transit_gateway_route_table_propagation(
        TransitGatewayRouteTableId=tgw_rt_id,
        TransitGatewayAttachmentId= tgw_att_id,
        DryRun=False
    )

#Create transit gateway multi-cast domain
def create_transit_gateway_multicast_domain(transit_gateway_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_multicast_domain(
        TransitGatewayId=transit_gateway_id,
        TagSpecifications=[
            {
                'ResourceType':  'transit-gateway-multicast-domain',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'aquis-terraform-boto3-tgw-multicast-domain'
                    },
                ]
            },
        ],
        DryRun=False
    )
    return response

#Associate transit gateway multi cast domain
def associate_transit_gateway_multicast_domain(tgw_multicast_domain_id, tgw_attachment_id, subnetID):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.associate_transit_gateway_multicast_domain(
    TransitGatewayMulticastDomainId=tgw_multicast_domain_id,
    TransitGatewayAttachmentId=tgw_attachment_id,
    SubnetIds=[
        subnetID,
    ],
    DryRun=False
    )
    return response

#Delete transit gateway multi-cast domain
def delete_transit_gateway_multicast_domain(tgwy_multicast_domain_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.delete_transit_gateway_multicast_domain(
        TransitGatewayMulticastDomainId=tgwy_multicast_domain_id,
        DryRun=False
    )
    return response

#Delete transit gateway vpc attachment
def delete_transit_gateway_vpc_attachment(transit_gateway_attachment_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.delete_transit_gateway_vpc_attachment(
        TransitGatewayAttachmentId=transit_gateway_attachment_id,
        DryRun=False
    )
    return response

#Delete transit gateway
def delete_transit_gateway(transit_gateway_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.delete_transit_gateway(
        TransitGatewayId=transit_gateway_id,
        DryRun=False
    )

# dissacotiate transit gateway multicast domain
def disassociate_transit_gateway_multicast_domain(tgw_multicast_domain_id, tgw_attachment_id, subnet_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.disassociate_transit_gateway_multicast_domain(
        TransitGatewayMulticastDomainId=tgw_multicast_domain_id,
        TransitGatewayAttachmentId=tgw_attachment_id,
        SubnetIds=[
            subnet_id,
        ],
        DryRun=False
    )
#register transit gateway multi-cast members
def register_transit_gateway_multicast_group_members(tgw_multicast_domain_id, group_address, network_interface3, network_interface4):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.register_transit_gateway_multicast_group_members(
    TransitGatewayMulticastDomainId = tgw_multicast_domain_id,
    GroupIpAddress = group_address,
    NetworkInterfaceIds = [
                            network_interface3, network_interface4,
                          ],
    DryRun = False
    )
    return response

def register_transit_gateway_multicast_group_sources(tgw_multicast_domain_id, nic1id, group_address):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.register_transit_gateway_multicast_group_sources(
        TransitGatewayMulticastDomainId=tgw_multicast_domain_id,
        GroupIpAddress=group_address,
        NetworkInterfaceIds=[
            nic1id,
        ],
        DryRun=False
    )
    return response
#Delete transit gateway route table
def delete_transit_gateway_route_table(rtb_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.delete_transit_gateway_route_table(
        TransitGatewayRouteTableId=rtb_id,
        DryRun=False
    )

if __name__ == '__main__':
    action = sys.argv[1]

    if action == "apply":

        #Get values from python input when calling python and assign to variables using sys.argv
        vpc_id = sys.argv[2]
        subnet_id = sys.argv[3]
        processor1nic = sys.argv[4]
        processor2nic = sys.argv[5]
        processor3nic = sys.argv[6]
        #Create transit gateway
        tgw_response = create_transit_gateway()
        #Collect transit gateway id from response
        tgw_id = tgw_response['TransitGateway']['TransitGatewayId']
        time.sleep(120)
        #Create transit gateway attachment
        tgw_attachment_response = create_transit_gateway_vpc_attachment(tgw_id, vpc_id, subnet_id)
        #get tgw attachment id response
        tgw_attachment_id = tgw_attachment_response['TransitGatewayVpcAttachment']['TransitGatewayAttachmentId']
        time.sleep(90)
        #Create transit gateway route table and get response
        tgw_rt_response = create_transit_gateway_rt(tgw_id)
        #Get transit gateway route table id from the response
        tgw_rt_id = tgw_rt_response ['TransitGatewayRouteTable']['TransitGatewayRouteTableId']
        time.sleep(90)
        #associate transit gateway route table
        associate_transit_gateway_route_table(tgw_rt_id,tgw_attachment_id)
        time.sleep(60)
        #enable transit gateway route table propogation
        enable_transit_gateway_route_table_propagation(tgw_rt_id, tgw_attachment_id)
        time.sleep(30)
        #Create transit gateway route
        create_transit_gateway_route(tgw_rt_id, "10.123.112.0/24", tgw_attachment_id)
        time.sleep(60)
        #Create transit gateway multi cast domain
        tgw_multicast_domain_response = create_transit_gateway_multicast_domain(tgw_id)
        #Get transit gateway multi cast domain id
        tgw_multicast_domain_id = tgw_multicast_domain_response['TransitGatewayMulticastDomain']['TransitGatewayMulticastDomainId']
        time.sleep(90)
        #Associate transit gateway multi-cast domain
        associate_transit_gateway_multicast_domain(tgw_multicast_domain_id, tgw_attachment_id, subnet_id)
        time.sleep(60)
        #register transit gateway multicast group members 1
        register_transit_gateway_multicast_group_members(tgw_multicast_domain_id, "224.3.2.2", processor2nic, processor3nic)
        time.sleep(60)
        #register transit gateway multicast group members 2
        register_transit_gateway_multicast_group_members(tgw_multicast_domain_id, "224.3.2.3", processor2nic, processor3nic)
        time.sleep(60)
        #register transit gateway multicast group sources 1
        register_transit_gateway_multicast_group_sources(tgw_multicast_domain_id,processor1nic, "224.3.2.3")
        # register transit gateway multicast group sources 2
        register_transit_gateway_multicast_group_sources(tgw_multicast_domain_id, processor1nic, "224.3.2.2")

    if action == "destroy":

        #Get values from python input when calling python and assign to variables using sys.argv
        transit_gateway_multicast_domain_id = sys.argv[2]
        transit_gateway_attachment_id = sys.argv[3]
        transit_gateway_id = sys.argv[4]
        subnet_id = sys.argv[5]
        rtb_id = sys.argv[6]

        #Dissacotiate transit gate way multicast domain with subnet
        disassociate_transit_gateway_multicast_domain(transit_gateway_multicast_domain_id, transit_gateway_attachment_id, subnet_id)
        time.sleep(120)
        #Delete transit gateway multicast domain
        delete_transit_gateway_multicast_domain(transit_gateway_multicast_domain_id)
        time.sleep(120)
        #Delete transit gateway VPC attachment
        delete_transit_gateway_vpc_attachment(transit_gateway_attachment_id)
        time.sleep(120)
        #Delete transit gateway
        delete_transit_gateway(transit_gateway_id)
        time.sleep(30)
        #Delete transit gateway route table
        delete_transit_gateway_route_table(rtb_id)




