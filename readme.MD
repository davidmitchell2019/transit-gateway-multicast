Creates a transit gateway multi-cast domain in N Virginia US_EAST-1

PLEASE RUN THESE COMMANDS TO BUILD

install aws cli

install terraform

install boto3 (pip install boto3) best to do from a virtual env

aws configure

Set access key, secret key and region to us-east-1
Terraform init

Terraform apply -auto-approve

python lambda-transit-gateway/transit-gateway.py apply $(terraform output vpc-id) $(terraform output subnet-id) $(terraform output processor1-nic) $(terraform output processor2-nic) $(terraform output processor3-nic) 

PLEASE RUN THESE COMMANDS TO DESTROY

please substitute values for 

-transit-gateway_multicast_domain_id 

-transit_gateway_attachment_id 

-transit_gateway_id 

-subnet_id

-route_table_id

You will need to get these from the portal

for example command:

python lambda-transit-gateway/transit-gateway.py destroy tgw-mcast-domain-04384954747d28e47 tgw-attach-09742505d138e6434 tgw-059bac79a0e09e6bb subnet-0e704af42e7eb8a8a tgw-rtb-0301cba83c4e527fc

terraform destroy -auto-approve 
