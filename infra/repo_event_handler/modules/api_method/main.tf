variable "rest_api_id" {}
variable "parent_id" {}
variable "path_part" {}
variable "http_method" {}
variable "function" {}
variable "globals" { type = "map" }

resource "aws_api_gateway_resource" "resource" {
  rest_api_id = "${var.rest_api_id}"
  parent_id = "${var.parent_id}"
  path_part = "${var.path_part}"
}

resource "aws_api_gateway_method" "method" {
  rest_api_id = "${var.rest_api_id}"
  resource_id = "${aws_api_gateway_resource.resource.id}"
  http_method = "${var.http_method}"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "integration" {
  rest_api_id = "${var.rest_api_id}"
  resource_id = "${aws_api_gateway_resource.resource.id}"
  http_method = "${aws_api_gateway_method.method.http_method}"
  type = "AWS"
  integration_http_method = "POST"
  uri = "arn:aws:apigateway:${var.globals["region"]}:lambda:path/2015-03-31/functions/arn:aws:lambda:${var.globals["region"]}:${var.globals["account"]}:function:${var.function}/invocations"
}

resource "aws_api_gateway_method_response" "200" {
  rest_api_id = "${var.rest_api_id}"
  resource_id = "${aws_api_gateway_resource.resource.id}"
  http_method = "${aws_api_gateway_method.method.http_method}"
  status_code = "200"
}

resource "aws_api_gateway_integration_response" "integration_response" {
  rest_api_id = "${var.rest_api_id}"
  resource_id = "${aws_api_gateway_resource.resource.id}"
  http_method = "${aws_api_gateway_method.method.http_method}"
  status_code = "${aws_api_gateway_method_response.200.status_code}"
  depends_on = ["aws_api_gateway_integration.integration"]
}

output "method_arn" { value = "arn:aws:execute-api:${var.globals["region"]}:${var.globals["account"]}:${var.rest_api_id}/*/${var.http_method}/${var.path_part}" }
