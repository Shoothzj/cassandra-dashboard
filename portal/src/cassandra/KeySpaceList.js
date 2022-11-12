/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import React, { useEffect, useState } from 'react';
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import {
  Box,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  TextField,
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import BACKEND_HOST from '../Const';

function KeySpaceList() {
  const columns = [{ field: 'keyspace', headerName: 'KeySpace', width: 300 }];

  const [keySpaces, setKeySpaces] = useState([]);

  const fetchKeySpaces = async () => {
    const response = await fetch(`${BACKEND_HOST}/api/cassandra/keyspaces`);
    const data = await response.json();
    setKeySpaces(data.map((aux) => ({ id: aux, keyspace: aux })));
  };

  const navigate = useNavigate();

  useEffect(() => {
    fetchKeySpaces();
  }, []);

  const handleEvent = (
    params, // GridRowParams
    event, // MuiEvent<React.MouseEvent<HTMLElement>>
    details, // GridCallbackDetails
  ) => {
    navigate(`/cassandra/keyspaces/${params.row.keyspace}`);
  };

  return (
    <div>
      <h1>KeySpace List</h1>
      <Box sx={{ height: 600, width: '100%' }}>
        <DataGrid
          onRowClick={handleEvent}
          rows={keySpaces}
          columns={columns}
          pageSize={10}
          rowsPerPageOptions={[10]}
          checkboxSelection
          disableSelectionOnClick
          experimentalFeatures={{ newEditingApi: true }}
          components={{ Toolbar: GridToolbar }}
        />
      </Box>
    </div>
  );
}

export default KeySpaceList;
