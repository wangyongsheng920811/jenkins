#!/bin/bash
ip=$1
project_name=$2
start_command=$3
stop_command=$4

echo "############ ip is $ip ############"
echo "############ project_name is $project_name ############"
echo "############ start_command is $start_command ############"
echo "############ stop_command is $stop_command ############"

ssh -Tq dingding@$ip << remote_ssh
. /etc/profile.d/nodejs.sh
npm config set registry http://registry.npm.taobao.org/
cd /home/dingding

if [ -d "$project_name.bak" ];then
echo "$project_name.bak  exists"
rm -rf $project_name.bak
else
echo "$project_name.bak did not exist"
fi

cd /home/dingding/$project_name/code && $stop_command || echo "stop server fail"
cd /home/dingding && mv $project_name $project_name.bak

exit
remote_ssh

cd /home/Jenkins/workspace
/usr/bin/rsync -avz $project_name/  dingding@$ip:/home/dingding/$project_name/

ssh -Tq dingding@$ip << remote_ssh

cd /home/dingding/$project_name/code && JENKINS_NODE_COOKIE=dontKillMe && npm install && $start_command

exit
remote_ssh