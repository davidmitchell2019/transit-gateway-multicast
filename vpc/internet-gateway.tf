resource "aws_internet_gateway" "gw" {
  vpc_id = "${aws_vpc.transit-gateway-vpc.id}"

  tags = {
    Name = "aquis-terraform-boto3-transit-gateway-igw"
  }
}
