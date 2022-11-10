import os

var_cassandra_host = os.getenv("CASSANDRA_HOST")

if var_cassandra_host is None:
    var_cassandra_host = "localhost"


class EnvConst:
    cassandra_host = var_cassandra_host
