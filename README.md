# DataOpsDemo
DockerCompose file with single node zookeeper and kafka (https://github.com/hermag/DataOpsDemo/blob/master/docker-composes/SingleNodeKafkaZK/docker-compose.yml) and not only.

#### Deployment of docker network required for the demo.
Before running the docker-compose up -d, one should create `kafka_net` the corresponding network 
```
docker network create kafka_net --subnet=16.168.0.0/16
```

#### Create topic.
```
docker exec singlenodekafkazk_kafka_1 kafka-topics --create --zookeeper singlenodekafkazk_zk1_1:2181 --replication-factor 1 --partitions 1 --topic test
```

#### Check if topic has created.
```
docker exec singlenodekafkazk_kafka_1 kafka-topics --describe --topic test --zookeeper singlenodekafkazk_zk1_1:2181
```

#### Use kafka console consumer
This command assumes that kafka is running as a docker container and it's name is singlenodekafkazk_kafka_1, name of the zookeeper container is singlenodekafkazk_zk1_1, the topic name is `test`.
```
docker exec singlenodekafkazk_kafka_1 kafka-console-consumer --zookeeper singlenodekafkazk_zk1_1:2181 --topic test
``` 
