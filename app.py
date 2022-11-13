###
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
###

import os

from flask import Flask, send_from_directory
from flask_cors import CORS

from api.cassandra_keyspace import cassandra_keyspace

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portal", "build")

print('root path is ' + root)

app = Flask(__name__, static_url_path='', static_folder=root)
CORS(app)
app.register_blueprint(cassandra_keyspace, url_prefix='/api/cassandra/keyspaces')


@app.route('/', methods=['GET'])
def redirect_to_index():
    return send_from_directory(root, 'index.html')


if __name__ == '__main__':
    app.run()
