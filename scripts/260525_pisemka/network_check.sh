#!/bin/bash

promena=$(ping -c 5 -W 5 192.168.10.1 | grep packet | awk '{print $7;}' | tr -d %)

# Send a single ping to 192.168.10.1 with a timeout of 5 seconds
if [ "$promena" != "0" ]; then
    logger "$(date): Ping failed, restarting network..."
    # Restart the network service (adjust for your system's service manager)
    sudo systemctl restart systemd-networkd
fi

# Zablokovani posilani ping requestu na 192.168.10.1
# sudo iptables -A INPUT -p icmp -s 192.168.10.1 -j DROP

# Povoleni
# sudo iptables -F

# Spusteni scriptu jednou za XYZ casu pres crontab
# crontab -e
# */5 * * * * /home/student/network_check.sh
