## Kafka
![kafka_pub_sub_메시지큐](/assets/kafka_pub_sub.webp)

> 무인택배함과 비슷한 개념
>
> 누가 받는지 / 수신자는 관심 없음 - 보내는 입장 (publisher) 의 역할만 - 보내기만 / kafka가 저장 => subscriber 입장에서는 보내온 데이터가 있다면 읽을뿐
>
>
> 'topic': kafka가 들어오는 데이터를 계속 쌓는 중간다리의 역할
>

## kafka 다운로드 
~위치에서 
```shell
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
```

- unzip
```shell
tar -zxvf kafka_2.13-3.9.0.tgz
```
- zookeeper 실행
```shell
bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
```
- kafka 실행
```shell
bin/kafka-server-start.sh -daemon config/server.properties
```

