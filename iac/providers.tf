terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-west-2"
}

resource "kubernetes_service" "LoadBalancer" {
  metadata {
    name = "load-balancer-flask-api"
  }
    port {
      port = 80
      target_port = 80
    }
    type = "LoadBalancer"
  }