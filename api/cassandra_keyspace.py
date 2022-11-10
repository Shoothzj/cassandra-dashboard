from cassandra.cluster import Cluster
from flask import Blueprint, request, jsonify

from const.constant import EnvConst

cassandra_keyspace = Blueprint('cassandra_keyspace', __name__)


@cassandra_keyspace.route('', methods=['GET'])
def get_keyspace_list():
    cluster = Cluster([EnvConst.cassandra_host])
    session = cluster.connect()
    result_set = session.execute("""
        DESC keyspaces
        """)
    keyspace_list = []
    for (keyspace_name, keyspace_type, name) in result_set:
        keyspace_list.append(keyspace_name)
    return jsonify(keyspace_list)


@cassandra_keyspace.route('/create', methods=['POST'])
def create_keyspace():
    request_data = request.get_json()
    cluster = Cluster([EnvConst.cassandra_host])
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE %s
        WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : %s }
        """ % (request_data['keyspace'], request_data['replication_factor']))
    return 'OK'


@cassandra_keyspace.route('/delete', methods=['POST'])
def delete_keyspace():
    request_data = request.get_json()
    cluster = Cluster([request_data['host']])
    session = cluster.connect()
    session.execute("""
        DROP KEYSPACE %s
        """ % request_data['keyspace'])
    return 'OK'
