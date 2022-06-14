provider "aws" {
    profile = "devops" 
    region = "us-east-1"
}
resource "aws_instance" "instance01" {
    ami = "ami-09d56f8956ab235b3"
    instance_type = "t2.micro" 
    tags = {
    "Name"        = "web-server"
    "environment" = "dev"
}
provisioner "local-exec" {
    command = "echo ${aws_instance.instance01.id} > instance_id.txt"
}
}
