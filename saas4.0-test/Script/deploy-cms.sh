port=52020
old_pid=$(ssh -tt root@192.168.2.73 lsof -t -i:$port)

ssh -tt root@192.168.2.73<< remote_ssh
echo "端口号为：$port"
if [ "$old_pid" == "" ];then
    echo "端口未占用"
else
    echo "端口被PID=$old_pid占用，正在清理占用程序..."
    kill -9 $old_pid
    fi

echo "备份qycms-boot.jar为qycms-boot.jarbak ..."
mv /var/fangqian/cms/qycms-boot.jar /var/fangqian/cms/qycms-boot.jarbak
echo "拷贝新qycms-boot.jar到当前路径..."
scp root@192.168.2.71:$WORKSPACE/code/qycms-boot.jar /var/fangqian/cms/qycms-boot.jar
cd /var/fangqian/cms
mv logs/log.log logs/log.logbak
echo "开始启动..."
nohup java -jar qycms-boot.jar --spring.profiles.active=test >>logs/log.log &
exit
remote_ssh
n=1
while true
do
    new_pid=$(ssh -tt root@192.168.2.73 lsof -t -i:$port)
    if [ "$new_pid" == "" ];then
        echo "正在启动程序..."
        if [ $n == 10 ];then
            echo "部署失败！"
            ssh -tt root@192.168.2.73 cat /var/fangqian/cms/logs/log.log           
            exit 1
        fi
        let n=n+1
        sleep 10
    else
        echo "程序启动完成"
        break;
    fi
done

echo "部署cms完成"