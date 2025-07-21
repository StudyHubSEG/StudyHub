#!/usr/bin/env python3

import subprocess
import time

# Start the telnet command
process = subprocess.Popen(
    ["g", "10.33.40.20", "telnet", "onie_reboot"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Wait for the rescue mode message to appear
while True:
    output = process.stdout.readline()
    print(output, end='')  # Show the output as it comes
    
    if "discover: Rescue mode detected.  Installer disabled." in output:
        break

# Hit enter to go into ONIE shell
process.stdin.write("\n")
process.stdin.flush()

# Wait a moment
time.sleep(2)

# Run the installer command
installer_cmd = "onie-nos-install http://artifactory.ciena.com/valimar-snapshot/01-11-02-0087/meta-onie-installer-core-aarch64/meta_10-11-02-0087-core-aarch64.registry-int.bin\n"
process.stdin.write(installer_cmd)
process.stdin.flush()

# Show remaining output
while True:
    output = process.stdout.readline()
    if not output:
        break
    print(output, end='')