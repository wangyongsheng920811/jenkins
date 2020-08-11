# 第一个参数为服务端口， 第二个参数为重命名的jar名，第三个参数是jar路径
function deploy(){
    port=$1
    server_name=$2
    jar_path=$3
    
    while true
    do
        old_pid=$(ps -ef | grep $server_name | grep java | grep -v grep | awk '{print $2}')
        echo "========================================================================"
        echo "server_name:$server_name || old_pid:$old_pid"
        
        if [ "$old_pid" == "" ];then
            echo "$server_name未启动"
            break
        else
            echo "$server_name被PID=$old_pid占用，正在清理占用程序..."
            kill -9 $old_pid
        fi
    done

    echo "拷贝新xx.jar到当前路径..."
    cp -f $jar_path/*.jar /root/jenkins/server/$server_name.jar
    cd /root/jenkins/server/
    rm ./$server_name.log
    echo "开始启动$server_name..."
    nohup java -jar -Xms128m -Xmx1024m $server_name.jar --spring.profiles.active=UAT>>$server_name.log 2>&1 &

    is_start $server_name $server_name.log
}

# 根据端口是否启动判断服务是否启动，第一个参数为判断的端口， 第二个参数为日志名
function is_start(){
    server_name=$1
    log_name=$2
    n=1
    while true
    do
        if grep -q "Started .*Application in" /root/jenkins/server/$log_name
        then
            echo "$server_name启动完成"
            echo "========================================================================"
            break
        else
            if [ $n == 10 ]
            then
                echo "$server_name部署失败！"
                cat /root/jenkins/server/$log_name
                exit 1
            fi
            let n=n+1
            sleep 10
        fi
        # new_pid=$(ps -ef | grep $server_name | grep java | grep -v grep | awk '{print $2}')
        # echo "server_name:$server_name || new_pid:$new_pid"
        # if [ "$new_pid" == "" ];then
            # echo "正在启动$server_name..."
            # if [ $n == 10 ];then
                # echo "$server_name部署失败！"
                # cat /root/jenkins/server/$log_name
                # exit 1
            # fi
            # let n=n+1
            # sleep 10
        # else
            # echo "$server_name启动完成"
            # echo "========================================================================"
            # break
        # fi
    done
}

api_port=$1
api_name=$2
api_path=$3

deploy $api_port $api_name $api_path
