output "controller-nic" {
  value = "${aws_instance.p1.primary_network_interface_id}"
}
output "processor1-nic" {
   value = "${aws_instance.p2.primary_network_interface_id}"
}
output "processor2-nic" {
   value = "${aws_instance.p3.primary_network_interface_id}"
}
output "processor3-nic" {
   value = "${aws_instance.p4.primary_network_interface_id}"
}