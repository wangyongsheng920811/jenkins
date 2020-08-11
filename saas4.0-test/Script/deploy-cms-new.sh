port=52020
old_pid=$(lsof -t -i:$port)

echo "端口号为：$port"
if [ "$old_pid" == "" ];then
    echo "端口未占用"
else
    echo "端口被PID=$old_pid占用，正在清理占用程序..."
    kill -9 $old_pid
    fi

echo "备份qycms-boot.jar为qycms-boot.jarbak ..."
mv /root/server/cms/qycms-boot.jar /root/server/cms/qycms-boot.jarbak
echo "拷贝新qycms-boot.jar到当前路径..."
cp $WORKSPACE/code/qycms-boot.jar /root/server/cms/qycms-boot.jar
cd /root/server/cms
mv logs/log.log logs/log.logbak
echo "开始启动..."
nohup java -jar qycms-boot.jar --spring.profiles.active=test >>logs/log.log &

n=1
while true
do
    new_pid=$(lsof -t -i:$port)
    if [ "$new_pid" == "" ];then
        echo "正在启动程序..."
        if [ $n == 10 ];then
            echo "部署失败！"
            cat /root/server/cms/logs/log.log           
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