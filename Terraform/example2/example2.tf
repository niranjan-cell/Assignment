provider "aws" { 
    region = "us-east-1"
    profile = "devops" 
    
}
resource "aws_instance" "instance01" {
    ami = "ami-09d56f8956ab235b3" 
    instance_type = "t2.micro" 
    tags = {
    "Name"        = "web-server"
    "environment" = "dev"
}
}
resource "aws_instance" "instance02" {
    ami = "ami-09d56f8956ab235b3"
    instance_type = "t2.micro" 
    tags = {
    "Name"        = "app-server"
    "environment" = "stage"
    }
}
