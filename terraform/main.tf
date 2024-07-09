terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_network" "my_app_network" {
  name = "my_app_network"
}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_image" "application" {
  name = "application:latest"
  build {
    context    = "${path.module}/../src"
    dockerfile = "Dockerfile"
  }
  keep_locally = false
}

resource "docker_container" "nginx_server" {
  image = docker_image.nginx.image_id
  count = 2
  name  = "nginx_server-${count.index + 1}"
  ports {
    internal = 80
    external = "808${count.index + 1}"
  }
  volumes {
    container_path = "/etc/nginx/conf.d/default.conf"
    host_path      = abspath("${path.module}/nginx.conf")
  }
  networks_advanced {
    name = docker_network.my_app_network.name
  }  
  command = ["nginx", "-g", "daemon off;"]

}

resource "docker_container" "application" {
  image = docker_image.application.image_id
  name  = var.app_name
  # env   = ["PORT=${var.application_server_port}"]
  ports {
    internal = var.application_server_port
    external = var.application_server_port
  }
  networks_advanced {
    name = docker_network.my_app_network.name
  }
}
