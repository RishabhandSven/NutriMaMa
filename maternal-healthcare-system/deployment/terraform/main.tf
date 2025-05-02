resource "aws_instance" "maternal_healthcare_backend" {
  ami           = "ami-0c55b159cbfafe1f0" # Replace with a valid AMI ID
  instance_type = "t2.micro"

  tags = {
    Name = "MaternalHealthcareBackend"
  }
}

resource "aws_security_group" "backend_sg" {
  name        = "backend_sg"
  description = "Allow traffic to the backend"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group_rule" "allow_http" {
  type              = "ingress"
  from_port        = 80
  to_port          = 80
  protocol         = "tcp"
  security_group_id = aws_security_group.backend_sg.id
  cidr_blocks      = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "allow_https" {
  type              = "ingress"
  from_port        = 443
  to_port          = 443
  protocol         = "tcp"
  security_group_id = aws_security_group.backend_sg.id
  cidr_blocks      = ["0.0.0.0/0"]
}

resource "aws_instance" "maternal_healthcare_redis" {
  ami           = "ami-0c55b159cbfafe1f0" # Replace with a valid AMI ID
  instance_type = "t2.micro"

  tags = {
    Name = "MaternalHealthcareRedis"
  }
}

resource "aws_security_group" "redis_sg" {
  name        = "redis_sg"
  description = "Allow traffic to Redis"

  ingress {
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "backend_instance_ip" {
  value = aws_instance.maternal_healthcare_backend.public_ip
}

output "redis_instance_ip" {
  value = aws_instance.maternal_healthcare_redis.public_ip
}