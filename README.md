# DataOpsDemo
DockerCompose file with single node zookeeper and kafka (https://github.com/hermag/DataOpsDemo/blob/master/docker-composes/SingleNodeKafkaZK/docker-compose.yml) and not only.

#### Deployment of docker network required for the demo.
Before running the docker-compose up -d, one should create `kafka_net` the corresponding network 
```
docker network create kafka_net --subnet=16.168.0.0/16
```
