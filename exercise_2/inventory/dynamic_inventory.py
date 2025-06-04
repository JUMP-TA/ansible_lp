#!/usr/bin/env python3
import json

inventory = {
    "web": {
        "hosts": ["192.168.56.11"],
        "vars": {
            "ansible_user": "vagrant",
            "ansible_ssh_private_key_file": "~/.ssh/id_rsa"
        }
    },
    "_meta": {
        "hostvars": {
            "192.168.56.11": {}
        }
    }
}

print(json.dumps(inventory))
