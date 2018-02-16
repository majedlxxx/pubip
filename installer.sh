#!/bin/bash
loc1=$(pwd)
echo "Do you want to install pubip[Y/N] (default=N)"
read op
if [ $op == 'y' ] || [ $op == 'Y' ] || [ $op == '\n' ]
then
  cp pubip /bin
  cd /bin
  chmod +x pubip
  cd
  mkdir publicIp
  cd publicIp
  loc2=$(pwd)
  cd $loc1
  cp pubip.py $loc2
  echo "Done"
  echo "To use it just type pubip"

else
  echo "As you like"
fi
