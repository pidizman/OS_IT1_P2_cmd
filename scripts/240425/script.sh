#!/bin/bash
prom="ahoj"
export prom="ahoj"
./vypis.sh
./vypis1.sh arg
prom=$((1+1))
echo $prom
prom=$((10/10))
echo $prom
prom=$prom"ahoj"
echo $prom
prom=`date +%d%m%Y`
echo $prom
tar cvfz $prom.tar.gz /etc/apt
if [ "$?" -eq "0" ];then
    echo "vse ok"
else
    echo "neco se pokazilo"
fi
if test -d ./test ; then
    echo "adresar existuje"
else
    echo "vytvarim adresar"
    mkdir test
fi
prom=`free | grep "Mem" | awk '{print $4;}'`
prom2=`free | grep "Mem" | awk '{print $6;}'`
suma=$(($prom+$prom2))
if [ $suma -ge "1000000" ]; then
    echo "pameti je dostatek"
else
    echo "pameti je malo"
fi
