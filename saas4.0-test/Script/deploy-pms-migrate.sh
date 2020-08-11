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

killPort 52212

cp -Rf $WORKSPACE/code/pms-migrate-server/dist/ /root/jenkins/pms-migrate/
cd /root/jenkins/pms-migrate/dist
mv start_log.log start_log.logbak
echo "开始启动..."
nohup /usr/local/jdk1.8.0_201/bin/java -jar pms-migrate.jar >>start_log.log 2>&1 &
n=1
while true
do
    new_pid=`lsof -t -i:52212`
    if [ "$new_pid" == "" ];then
        echo "正在启动程序$n..."
        if [ $n == 12 ];then
            echo "部署失败！"
            cat log/start_log.log
            exit 1
        fi
        let n=n+1
        sleep 10
    else
        echo "程序启动完成"
        break;
    fi
done

echo "部署pms-migrate完成"