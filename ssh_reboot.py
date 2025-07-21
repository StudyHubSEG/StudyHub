#!/usr/bin/env python3

import subprocess
import sys

# Get IP address from user
ip = input("Enter IP address: ")

# Execute SSH with multiple commands
try:
    # Run the three commands in sequence
    subprocess.run(['ssh', ip, 'diag shell host; sudo onie reboot'])
    print(f"Commands sent to {ip}")
except Exception as e:
    print(f"Error: {e}")