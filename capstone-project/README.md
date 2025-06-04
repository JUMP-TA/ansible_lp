# Ansible Capstone Project: Automated CI/CD Pipeline

## Project Overview

In this capstone project, you'll leverage the complete set of Ansible skills developed throughout your learning journey to build and deploy a professional-grade automated CI/CD pipeline. This pipeline will handle cloud infrastructure provisioning, containerized application deployment, and comprehensive validation tests.

## Objectives

* **Provision AWS Cloud Infrastructure:**

  * Set up EC2 instances with proper security groups and networking

* **Dynamic Inventory Management:**

  * Configure AWS EC2 dynamic inventory for automated infrastructure management

* **Deploy Containerized Application:**

  * Use Docker Compose for deployment
  * Utilize Jinja2 templates for dynamic configuration

* **Secure Handling of Credentials:**

  * Integrate Ansible Vault for securing sensitive information

* **Robust Error Handling:**

  * Employ advanced error-handling techniques (block, rescue, always)

* **Task Delegation and Validation:**

  * Perform validation tasks from the control node

* **Documentation and Modular Structure:**

  * Clearly structured roles, templates, and playbooks
  * Comprehensive documentation for maintainability

## Project Structure

```
capstone-project/
├── ansible.cfg
├── inventory/
│   └── aws_ec2.yml
├── group_vars/
│   └── all.yml
├── roles/
│   ├── provision/
│   ├── docker_setup/
│   └── app_deploy/
├── playbooks/
│   └── deploy_pipeline.yml
├── vault/
│   └── secrets.yml
└── README.md
```

## Steps to Completion

### 1. Setup Dynamic Inventory

* Configure EC2 inventory plugin with regions and tag filters.
* Verify the dynamic inventory setup via CLI tests.

### 2. Provision Infrastructure

* Create role tasks for EC2 instance creation, specifying instance types and security groups.
* Configure VPC and subnetting as needed.

### 3. Implement Modular Roles

* `provision`: Provision EC2 instances and networking
* `docker_setup`: Install Docker and Docker Compose
* `app_deploy`: Deploy application with templated Docker Compose files

### 4. Deploy Dockerized Application

* Template `docker-compose.yml` using Jinja2
* Configure environment variables for Docker deployment

### 5. Secure Sensitive Information with Vault

* Encrypt AWS credentials and app secrets using Ansible Vault
* Reference encrypted secrets in playbooks

### 6. Implement Comprehensive Error Handling

* Use `block`, `rescue`, and `always` in tasks to handle deployment errors gracefully
* Document common error scenarios and resolutions

### 7. Perform Task Delegation and Deployment Validation

* Create delegated tasks for post-deployment validation
* Verify app availability through automated checks from the control node

## Final Deliverables

* Fully automated and documented CI/CD pipeline
* Secure management of sensitive credentials
* Validated and tested infrastructure and application deployment

## Trainer’s Note

This project integrates everything you've learned about Ansible and DevOps best practices. Upon completion, you'll have a robust, secure, and maintainable CI/CD pipeline suitable for real-world applications.