# Beginner Ansible Exercise: "Get Set, Automate!"

## Scenario

You've just joined a small DevOps team at a startup that’s rapidly scaling its web infrastructure. Your first task is to automate the installation and configuration of a basic NGINX web server on a new virtual machine. The infrastructure team has provided you with SSH access to a test server and wants you to demonstrate that you can use Ansible to deploy, configure, and verify a working web server using a simple playbook.

## Objectives

- Configure a basic Ansible environment
- Create a static inventory file
- Use Ansible modules to gather system facts
- Write and run a playbook that:
  - Installs NGINX
  - Ensures the service is running and enabled
- Validate your setup by accessing the web server

## Repository Structure
```
beginner-exercise/
├── README.md # This file
├── ansible.cfg # Ansible configuration file
├── inventory/
│ └── hosts # Static inventory file
├── playbooks/
│ └── webserver.yml # Your main playbook
```

## Instructions

### 1. Configure Your Environment

- Ensure Ansible is installed (`ansible --version`)
- Ensure you can SSH into the target server without a password prompt (SSH key-based auth)
- Replace the IP and username in `inventory/hosts` with your target VM details

### 2. Test Connectivity

Run the following command to test your Ansible connection:

```bash
ansible web -m ping
```

You should see a "pong" response from the host.

### 3. Create Your Playbook
Edit playbooks/webserver.yml to perform the following tasks:

Install nginx using the apt module

Ensure the nginx service is started and enabled using the service module

### 4. Execute Your Playbook
Run:
```bash
ansible-playbook playbooks/webserver.yml
```

### 5. Validate the Result
Open a browser and navigate to the IP address of your VM.

You should see the default NGINX welcome page.

Alternatively, use curl to test:
```bash
curl http://<your-server-ip>
```

### 6. Bonus: Gather Facts
Use the setup module to inspect facts about your target machine:

```bash
ansible web -m setup
```

Look for facts like ansible_distribution, ansible_hostname, etc.

## Success Criteria
Your playbook runs without error

NGINX is installed and running

You can access the web server in a browser or with curl

You’ve successfully gathered facts from the target host

## Summary
This exercise introduces core Ansible concepts: configuration, inventories, modules, and playbooks. It establishes a working environment that you’ll expand upon in future exercises.