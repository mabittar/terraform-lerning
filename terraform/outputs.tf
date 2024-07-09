output "nginx_server_image_id" {
  description = "ID of the nginx_server image"
  value       = docker_image.nginx.id
}

output "nginx_server_container_id" {
  description = "ID of the nginx_server container"
  value       = [docker_container.nginx_server.*.id]
}

output "application_image_id" {
  description = "ID of the application image"
  value       = docker_image.application.id
}

output "application_container_id" {
  description = "ID of the application container"
  value       = docker_container.application.id
}

output "application_running_port" {
  description = "Port of the application"
  value       = var.application_server_port
}
