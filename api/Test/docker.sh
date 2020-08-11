job_name=$1
api_branch=$2
web_branch=$3

cd docker/${job_name:7:-9}
if [ "$job_name" = "docker-saas-api-pipeline" ]; then
    container=${job_name:7:-9}${api_branch:7}"_web_1"
    m=7100
    n=7199
fi
if [ "$job_name" = "docker-saas-manage-pipeline" ]; then
    container=${job_name:7:-9}${api_branch:7}"_web_1"
    m=7200
    n=7299
fi
if [ "$job_name" = "docker-queue-service-pipeline" ]; then
    container=${job_name:7:-9}${api_branch:7}"_queue-service_1"
    create_conf
    deploy_docker
    exit $?
fi
if [ "$job_name" = "docker-open-api-pipeline" ]; then
    container=${job_name:7:-9}${api_branch:7}"_open-api_1"
    m=7300
    n=7399
fi

port=$(docker port $container|awk -F ':' '{print $2}')
if [ -z "$port" ]; then 
    echo "$container is new, start search a new port"
    for ((i=$m; i<=$n; i++))
    do
        res=$(lsof -i:$i)
        if [ -z "$res" ]; then
            echo "port $i is not used"
            break
        else
            echo "port $i is already used, continue searching"
        fi
    done
    new_port=$i
else
    echo "$container is already run on $port"
    new_port=$port
fi
echo "$new_port" > port.txt

create_conf
deploy_docker

function deploy_docker(){
    docker login -u tanzhiqiang -p Tanzhiqiang@2019 https://test-docker-hub.dding.net
    docker-compose pull
    docker-compose -p ${job_name:7:-9}${api_branch:7} down
    docker-compose -p ${job_name:7:-9}${api_branch:7} up -d
    docker logout https://test-docker-hub.dding.net
}

function create_conf(){
    sed -i "s/API_TAG/${api_branch:7}/g" docker-compose.yml
    sed -i "s/WEB_TAG/${web_branch:7}/g" docker-compose.yml
    sed -i "s/RUN_PORT/$new_port/g" docker-compose.yml
}