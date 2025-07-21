#!/usr/bin/env python3

import pexpect

# Run the initial command
child = pexpect.spawn("g 10.33.40.20 telnet onie_reboot")

# Wait for the rescue mode message
child.expect("discover: Rescue mode detected.  Installer disabled.")

# Press ENTER
child.sendline("")

# Run the installation command
child.sendline("onie-nos-install http://artifactory.ciena.com/valimar-snapshot/01-11-02-0087/meta-onie-installer-core-aarch64/meta_10-11-02-0087-core-aarch64.registry-int.bin")

# Show output
child.interact()