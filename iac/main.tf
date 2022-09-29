provider "aws" {
    version = "~> 2.0"
    region = "us-east-1"
}

resource "aws_instance" "dev" {
  count = 3  
  ami = var.amis["ubuntu-us-east-1"]
  instance_type = "t2.micro"
  key_name = "terraform-aws"
  tags =  {
    Name = "dev${count.index}"
  }
  vpc_security_group_ids = ["${aws_security_group.ssh-acess.id}"]
}