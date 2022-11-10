import { useParams } from 'react-router';
import React from 'react';

function KeySpacePage() {
  const { keyspace } = useParams();

  return (
    <div>
      <h1>
        KeySpace:
        {keyspace}
      </h1>
    </div>
  );
}

export default KeySpacePage;
