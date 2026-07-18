terraform {
  backend "s3" {
    bucket         = "github-actions-eks-dev-tfstate-575589967956"
    key            = "dev/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "github-actions-eks-dev-lock"
    encrypt        = true
  }
}