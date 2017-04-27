## Kafka Logger for Python

### Why this exists?

There's an existing python package that can send log to logstash through Kafka,
but it has two problems:

1. It's built on top of a specific python kafka package and it's outdated,
which left user no choice on which Kafka they can use.
2. It only uses default log formatting from python logging package,
which doesn't provide much useful information.

### Install

    pip install kafka-logger

### Usage

    import logging
    import KafkaLoggingHandler
    logger = logging.getLogger('python-logstash-logger')
    logger.setLevel(logging.INFO)
    log_producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
    logger.addHandler(KafkaLoggingHandler(log_producer, 'app-log'))
