provider "aws" {
    region = "us-east-1"
    access_key = "AKIASZBQWJUN2NITEKIG"
    secret_key = "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"
}
resource "aws_instance" "instance01" {
    ami = "ami-09d56f8956ab235b3"
    instance_type = "t2.micro"
}

