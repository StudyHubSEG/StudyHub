#!/usr/bin/env python3

import subprocess
import sys

# Get IP address from user
ip = input("Enter IP address: ")

# Execute SSH reboot command
try:
    subprocess.run(['ssh', ip, 'sudo', 'reboot'])
    print(f"Reboot command sent to {ip}")
except Exception as e:
    print(f"Error: {e}")