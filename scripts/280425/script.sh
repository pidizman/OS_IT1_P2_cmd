#!/bin/bash

while true; do
    # Command to be executed every 10 seconds
    prom=$(grep eno1 /proc/net/dev)
    read -a array <<< "$prom"
    time=$(date +"%s")
    echo "$time;${array[0]};${array[1]}" >> /tmp/monitoring.txt
    sleep 10
done
