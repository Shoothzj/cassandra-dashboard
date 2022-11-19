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

var_cassandra_host = os.getenv("CASSANDRA_HOST")
var_cassandra_username = os.getenv("CASSANDRA_USERNAME")
var_cassandra_password = os.getenv("CASSANDRA_PASSWORD")

if var_cassandra_host is None:
    var_cassandra_host = "localhost"

if var_cassandra_username is None:
    var_cassandra_username = ""

if var_cassandra_password is None:
    var_cassandra_password = ""
class EnvConst:
    cassandra_host = var_cassandra_host
    cassandra_username = var_cassandra_username
    cassandra_password = var_cassandra_password
