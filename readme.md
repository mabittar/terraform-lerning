# Learn Terraform - Nginx

[![Build Status](https://github.com/your-username/learn-terraform/workflows/Terraform%20Build/badge.svg)](https://github.com/your-username/learn-terraform/actions?query=workflow%3ATerraform+Build)
[![Terraform](https://www.terraform.io/assets/badge.svg)](https://www.terraform.io/)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Platform-blue)](https://cloud.google.com/)

This repository demonstrates how to deploy a simple Nginx web server using Terraform on Google Cloud Platform.

## Prerequisites

* Google Cloud Platform account with billing enabled.
* Terraform installed on your local machine.
* [Google Cloud SDK](https://cloud.google.com/sdk) installed and configured.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/learn-terraform.git
   cd learn-terraform
   ```

2. **Initialize Terraform:**

   ```bash
    cd terraform
    terraform init
   ```

3. **Create Terraform Plan:**

   ```bash
    terraform plan -out terraform.plan

   ```

4. **Inspect the plan:** Review the plan output to ensure it matches your expectations.

5. **Apply the Plan:**

    ```bash
    terraform apply "terraform.plan"
    ```

6. **Check the deployment:**
    * Open a web browser and navigate to
    `http://localhost:8081/html`.
    * You should see the Nginx welcome page.

7. **Destroy the infrastructure:**

    ```bash
    terraform destroy -auto-approve
   ```

## Configuration

The `terraform/modules/nginx/nginx.conf` file contains the Nginx configuration. You can customize this file to suit your needs.

## Notes

- This example uses a simple Nginx configuration. You can add more features and customizations as needed.
* The `<http://localhost:8081/html>` URL is a placeholder. You may need to adjust this based on your specific deployment.
- This example uses a basic Terraform configuration. - You can add more advanced features and best practices as you gain experience.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
