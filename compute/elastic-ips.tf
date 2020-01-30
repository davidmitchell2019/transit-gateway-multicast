resource "aws_eip" "controller" {
  instance = "${aws_instance.p1.id}"
  vpc      = true
}
resource "aws_eip" "processor1" {
  instance = "${aws_instance.p2.id}"
  vpc      = true
}
resource "aws_eip" "processor2" {
  instance = "${aws_instance.p3.id}"
  vpc      = true
}
resource "aws_eip" "processor3" {
  instance = "${aws_instance.p4.id}"
  vpc      = true
}