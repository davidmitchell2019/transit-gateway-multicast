output "vpc-id" {
  value = "${module.vpc.vpc-id}"
}
output "subnet-id" {
  value = "${module.vpc.subnet-id}"
}
output "controller-nic" {
  value = "${module.compute.controller-nic}"
}
output "processor1-nic" {
   value = "${module.compute.processor1-nic}"
}
output "processor2-nic" {
   value = "${module.compute.processor2-nic}"
}
output "processor3-nic" {
   value = "${module.compute.processor3-nic}"
}