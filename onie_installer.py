#!/usr/bin/env python3
"""
Simple ONIE installer script that automates the telnet connection and installation process.
"""

import pexpect
import sys
import time

def main():
    try:
        print("Starting ONIE installation process...")
        
        # Run the initial command
        print("Executing: g 10.33.40.20 telnet onie_reboot")
        child = pexpect.spawn("g 10.33.40.20 telnet onie_reboot")
        
        # Set a longer timeout since the command takes a while
        child.timeout = 300  # 5 minutes timeout
        
        # Wait for the rescue mode message
        print("Waiting for rescue mode message...")
        child.expect("discover: Rescue mode detected.  Installer disabled.")
        print("Rescue mode detected! Pressing ENTER to enter ONIE shell...")
        
        # Press ENTER to go into the ONIE shell
        child.sendline("")
        
        # Wait a moment for the shell to be ready
        time.sleep(2)
        
        # Send the installation command
        install_cmd = "onie-nos-install http://artifactory.ciena.com/valimar-snapshot/01-11-02-0087/meta-onie-installer-core-aarch64/meta_10-11-02-0087-core-aarch64.registry-int.bin"
        print(f"Running installation command: {install_cmd}")
        child.sendline(install_cmd)
        
        # Keep the session alive and show output
        print("Installation started. Monitoring output...")
        child.interact()
        
    except pexpect.TIMEOUT:
        print("Timeout occurred. The command might be taking longer than expected.")
        print("Current output:")
        print(child.before.decode('utf-8', errors='ignore'))
        sys.exit(1)
        
    except pexpect.EOF:
        print("Connection closed unexpectedly.")
        sys.exit(1)
        
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        child.close()
        sys.exit(1)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()