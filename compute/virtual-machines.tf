#Controller instance 1
resource "aws_instance" "p1" {
  ami           = "${var.controller-ami}"
  instance_type = "${var.controller-instance-type}"
  placement_group = "${aws_placement_group.multicast-reciever.id}"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"
  iam_instance_profile = "${aws_iam_instance_profile.tgw_profile.name}"
  key_name = "${var.key-name}"
  vpc_security_group_ids = ["${aws_security_group.allow_ssh.id}"]
  private_ip ="10.123.112.20"
  user_data = <<-EOF
              #!/bin/bash
              bash /tmp/aquis.sh
              EOF
  tags = {
    Name = "control-1"
  }
}
#Processor instance 1
resource "aws_instance" "p2" {
  ami           = "${var.processor-ami}"
  instance_type = "${var.processor-instance-type}"
  placement_group = "${aws_placement_group.multicast-reciever.id}"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"
  key_name = "${var.key-name}"
  vpc_security_group_ids = ["${aws_security_group.allow_ssh.id}"]
  private_ip ="10.123.112.51"
  user_data = <<-EOF
              #!/bin/bash
              bash /tmp/aquis.sh
              EOF
  tags = {
    Name = "processor-1"
  }
}
#Processor instance 2
resource "aws_instance" "p3" {
  ami           = "${var.processor-ami}"
  instance_type = "${var.processor-instance-type}"
  placement_group = "${aws_placement_group.multicast-reciever.id}"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"
  key_name = "${var.key-name}"
  vpc_security_group_ids = ["${aws_security_group.allow_ssh.id}"]
  private_ip ="10.123.112.52"
  user_data = <<-EOF
              #!/bin/bash
              bash /tmp/aquis.sh
              EOF
  tags = {
    Name = "processor-2"
  }
}
#Processor instance 3
resource "aws_instance" "p4" {
  ami           = "${var.processor-ami}"
  instance_type = "${var.processor-instance-type}"
  placement_group = "${aws_placement_group.multicast-reciever.id}"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"
  key_name = "${var.key-name}"
  vpc_security_group_ids = ["${aws_security_group.allow_ssh.id}"]
  private_ip ="10.123.112.53"
  user_data = <<-EOF
              #!/bin/bash
              bash /tmp/aquis.sh
              EOF
  tags = {
    Name = "processor-3"
  }
}
