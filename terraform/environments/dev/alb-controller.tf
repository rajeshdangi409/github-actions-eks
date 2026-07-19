resource "kubernetes_service_account" "aws_load_balancer_controller" {
  metadata {
    name      = "aws-load-balancer-controller"
    namespace = "kube-system"

    annotations = {
      "eks.amazonaws.com/role-arn" = aws_iam_role.aws_load_balancer_controller.arn
    }
  }
}

resource "helm_release" "aws_load_balancer_controller" {
  name       = "aws-load-balancer-controller"
  repository = "https://aws.github.io/eks-charts"
  chart      = "aws-load-balancer-controller"
  version    = "1.14.0"

  namespace = "kube-system"

  depends_on = [
    kubernetes_service_account.aws_load_balancer_controller
  ]

  set = [
  {
    name  = "clusterName"
    value = module.eks.cluster_name
  },
  {
    name  = "serviceAccount.create"
    value = "false"
  },
  {
    name  = "serviceAccount.name"
    value = "aws-load-balancer-controller"
  },
  {
    name  = "region"
    value = var.aws_region
  },
  {
    name  = "vpcId"
    value = module.vpc.vpc_id
  }
]
}
