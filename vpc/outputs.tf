output "vpc-id" {
  value = "${aws_vpc.transit-gateway-vpc.id}"
}
output "subnet-id" {
  value = "${aws_subnet.transit-gateway-subnet.id}"
}