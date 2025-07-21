#!/usr/bin/env python3
"""
SSH Reboot Script
This script connects to a remote machine via SSH and executes a reboot command.
"""

import subprocess
import sys
import re

def validate_ip_address(ip):
    """Validate if the provided string is a valid IP address."""
    pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

def ssh_reboot(ip_address):
    """Execute SSH command to reboot the remote machine."""
    try:
        # SSH command to connect and execute reboot
        ssh_command = [
            'ssh',
            '-o', 'StrictHostKeyChecking=no',  # Disable host key checking for automation
            '-o', 'ConnectTimeout=10',          # Set connection timeout
            ip_address,
            'sudo', 'reboot'
        ]
        
        print(f"Connecting to {ip_address} and executing reboot command...")
        print("Command:", ' '.join(ssh_command))
        
        # Execute the SSH command
        result = subprocess.run(
            ssh_command,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"✓ Reboot command sent successfully to {ip_address}")
            if result.stdout:
                print("Output:", result.stdout)
        else:
            print(f"✗ Error executing reboot command on {ip_address}")
            if result.stderr:
                print("Error:", result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"✗ SSH connection to {ip_address} timed out")
        return False
    except subprocess.CalledProcessError as e:
        print(f"✗ SSH command failed: {e}")
        return False
    except FileNotFoundError:
        print("✗ SSH client not found. Please install OpenSSH client.")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False
    
    return True

def main():
    """Main function to get IP address from user and execute SSH reboot."""
    print("SSH Reboot Script")
    print("=" * 20)
    
    while True:
        # Get IP address from user
        ip_address = input("Enter the IP address of the remote machine: ").strip()
        
        if not ip_address:
            print("✗ IP address cannot be empty. Please try again.")
            continue
            
        # Validate IP address format
        if not validate_ip_address(ip_address):
            print("✗ Invalid IP address format. Please enter a valid IP address (e.g., 192.168.1.100)")
            continue
            
        break
    
    # Confirm the action
    confirm = input(f"Are you sure you want to reboot the machine at {ip_address}? (y/N): ").strip().lower()
    
    if confirm not in ['y', 'yes']:
        print("Operation cancelled.")
        sys.exit(0)
    
    # Execute the SSH reboot command
    success = ssh_reboot(ip_address)
    
    if success:
        print(f"\n✓ Reboot command completed for {ip_address}")
        print("Note: The remote machine should be rebooting now.")
    else:
        print(f"\n✗ Failed to reboot {ip_address}")
        sys.exit(1)

if __name__ == "__main__":
    main()