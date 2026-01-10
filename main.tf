
provider "aws" {
  region = "ap-south-1"
}

# Fetch latest Windows Server 2022 AMI
data "aws_ami" "windows" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["Windows_Server-2022-English-Full-Base-*"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Security Group for RDP
resource "aws_security_group" "rdp" {
  name        = "windows-rdp-sg"
  description = "Allow RDP"
  vpc_id      = "vpc-08f660727bd4290a8" # Replace with your VPC ID

  ingress {
    from_port   = 3389
    to_port     = 3389
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # For testing; restrict later
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "windows" {
  ami                         = data.aws_ami.windows.id
  instance_type               = "t3.small"
  key_name                    = "key_1"
  subnet_id                   = "subnet-02ea2a454280dfb1e" # Replace with your subnet ID
  vpc_security_group_ids      = [aws_security_group.rdp.id]
  associate_public_ip_address = true

  tags = {
    Name = "simple-windows-ec2"
  }
}

# Outputs
output "public_ip" {
  value = aws_instance.windows.public_ip
}
