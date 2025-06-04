# Intermediate Ansible Exercise: "Modular Ops: Secure & Scalable"

## Scenario

You've been promoted to work on scalable, secure automation for the same web infrastructure team. The company is growing, and infrastructure-as-code principles are being adopted across the board. This time, you're expected to write modular, maintainable Ansible code that uses roles, variables, templating, dynamic inventory, and Ansible Vault to deploy a fully templated NGINX web server.

## Objectives

- Use a **dynamic inventory script**
- Create and apply a **custom role**
- Use **group variables** for reusable config
- Render a **Jinja2 template**
- Include **encrypted secrets** with **Ansible Vault**
- Deploy a system end-to-end using `site.yml`

## Repository Structure

```
intermediate-exercise/
├── ansible.cfg
├── inventory/
│   └── dynamic_inventory.py
├── group_vars/
│   └── all.yml
├── roles/
│   └── web/
│       ├── tasks/
│       │   └── main.yml
│       └── templates/
│           └── index.html.j2
├── playbooks/
│   └── site.yml
├── vault/
│   ├── secrets.yml
│   └── .vault_pass.txt
└── README.md
```

## Instructions

### 1. Verify Environment Setup

- Ensure Ansible is installed
- Ensure you have SSH access to your VM at the IP used in the inventory script
- Ensure Python is installed on the target system
- Mark the inventory script as executable:

```
chmod +x inventory/dynamic_inventory.py
```

### 2. Customize Inventory

Edit `inventory/dynamic_inventory.py` to include your target machine’s IP and SSH credentials.

Test inventory script:

```
ansible-inventory -i inventory/dynamic_inventory.py --list
```

### 3. Review the Role

Look at `roles/web/tasks/main.yml` and `templates/index.html.j2`. Understand how NGINX is installed and how the homepage is templated.

### 4. Configure Variables

Edit `group_vars/all.yml` to change the site title.

Example:

```
site_title: "Welcome to Production Alpha"
```

### 5. Encrypt Secrets

The `vault/secrets.yml` file contains sensitive information. It must be encrypted before use:

```
ansible-vault encrypt vault/secrets.yml
```

Ensure `.vault_pass.txt` contains the correct vault password and that `ansible.cfg` references it.

### 6. Run the Playbook

Execute the full deployment:

```
ansible-playbook playbooks/site.yml
```

### 7. Validate Deployment

Open a browser or use curl to access the deployed server at its IP. You should see the custom title and hostname rendered.

Example:

```
curl http://192.168.56.11
```

### 8. Inspect Vault Integration (Optional)

Decrypt and inspect:

```
ansible-vault view vault/secrets.yml
```

## Success Criteria

- Dynamic inventory returns correct hosts
- Role executes cleanly and is reusable
- Template renders with correct title and hostname
- Vault-encrypted file is used in playbook
- NGINX serves the generated template
- No tasks fail

## Summary

This exercise reinforces modular Ansible development with real-world elements: inventory automation, templating, variable management, and secrets handling. It prepares you for scalable production infrastructure as code.
