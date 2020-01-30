resource "aws_internet_gateway" "gw" {
  vpc_id = "${aws_vpc.transit-gateway-vpc.id}"

  tags = {
    Name = "terraform-boto3-transit-gateway-igw"
  }
}
