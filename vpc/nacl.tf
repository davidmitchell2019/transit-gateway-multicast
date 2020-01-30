resource "aws_network_acl" "nacl" {
  vpc_id = "${aws_vpc.transit-gateway-vpc.id}"
}
resource "aws_network_acl_rule" "nacl-rule" {
  network_acl_id = "${aws_network_acl.nacl.id}"
  protocol = "-1"
  rule_action = "allow"
  rule_number = 50
  cidr_block = "0.0.0.0/0"
  egress = "false"
}
resource "aws_network_acl_rule" "nacl-rule2" {
  network_acl_id = "${aws_network_acl.nacl.id}"
  protocol = "-1"
  rule_action = "allow"
  rule_number = 50
  cidr_block = "0.0.0.0/0"
  egress = "true"
}