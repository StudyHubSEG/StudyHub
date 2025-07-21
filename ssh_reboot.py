#!/usr/bin/env python3

import subprocess
import sys

# Get IP address from user
ip = input("Enter IP address: ")

# Execute SSH command with the onie reboot command
try:
    subprocess.run(['ssh', ip, 'sudo', 'onie', 'reboot'])
    print(f"ONIE reboot command sent to {ip}")
except Exception as e:
    print(f"Error: {e}")