resource "aws_subnet" "transit-gateway-subnet" {
  cidr_block = "${var.subnet-mask}"
  vpc_id = "${aws_vpc.transit-gateway-vpc.id}"
  availability_zone = "${var.avaialabilty-zone}"
  depends_on = ["aws_vpc.transit-gateway-vpc"]
  map_public_ip_on_launch = "true"

  tags = {
    Name = "terraform-boto3-transit-gateway-subnet"
  }
}
