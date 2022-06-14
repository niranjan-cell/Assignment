provider "aws" {
    region = "us-east-1" 
    profile = "devops"
}
resource "aws_instance" "instance01" {
    ami = "ami-09d56f8956ab235b3"  
    availability_zone = "us-east-1a"
    instance_type = "t2.micro" 
    tags = {
    "Name"        = "web-server"
    "environment" = "dev"
    }
depends_on = [aws_ebs_volume.diskSize]
}
resource "aws_ebs_volume" "diskSize" {
    availability_zone = "us-east-1a"
    size = 10
}
resource "aws_volume_attachment" "ebs_add" {
    device_name = "/dev/xvdf" 
    volume_id   = aws_ebs_volume.diskSize.id 
    instance_id = aws_instance.instance01.id
}
resource "aws_eip" "elastic_ip" {
    instance = aws_instance.instance01.id 
    vpc = true
}
