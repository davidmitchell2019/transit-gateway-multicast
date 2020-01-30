module "vpc" {
  source = "./vpc"
  avaialabilty-zone = "${var.availability-zone}"
  subnet-mask = "${var.subnet-mask}"
}
module "compute" {
  source = "./compute"
  availability-zone = "us-east-1a"
  subnet-id = "${module.vpc.subnet-id}"
  vpc-id = "${module.vpc.vpc-id}"
  key-name = "${var.key-name}"
  controller-instance-type = "${var.controller-instance-type}"
  processor-instance-type = "${var.processor-instance-type}"
  controller-ami = "${var.controller-ami}"
  processor-ami = "${var.processor-ami}"
}