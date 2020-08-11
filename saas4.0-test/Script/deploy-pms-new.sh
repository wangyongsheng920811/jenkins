echo "开始部署pms..."
killPort(){
    port=$1
    echo "端口号为：$port"
    old_pid=`netstat -lnp | grep $port | awk '{print $7}' | awk -F '/' '{print $1}'`
    if [ "$old_pid" == "" ];then
        echo "端口未占用"
    else
        echo "端口被PID=$old_pid占用，正在清理占用程序..."
        kill -9 `lsof -t -i:$port`
    fi
}

killPort 52001

cd /root/server/pms
echo "备份qypms-boot.jar为qypms-boot.jarbak ..."
mv qypms-boot.jar qypms-boot.jarbak
echo "拷贝新qypms-boot.jar到当前路径..."
# scp -P 4399 root@118.31.46.211:/root/jenkins/workspace/saas-pms-api-pipeline/code/qypms-boot.jar ./
cp $WORKSPACE/code/qypms-boot.jar /root/server/pms/qypms-boot.jar
mv logs/log.log logs/log.logbak
rm -rf /root/server/pms/lib
cp -r /root/jenkins/workspace/saas-pms-api-pipeline/code/lib/ ./

echo "开始启动..."
nohup java -jar qypms-boot.jar --spring.profiles.active=test >>logs/log.log 2>&1 &
n=1
while true
do
    new_pid=`lsof -t -i:52001`
    if [ "$new_pid" == "" ];then
        echo "正在启动程序$n..."
        if [ $n == 12 ];then
            echo "部署失败！"
            cat logs/log.log
            exit 1
        fi
        let n=n+1
        sleep 10
    else
        echo "程序启动完成"
        break;
    fi
done

echo "部署pms完成"