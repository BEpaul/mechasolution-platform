import { Card } from 'antd';
import React from 'react';

const App = (props) => (
  <>
    <Card
      title={props.title}
      extra={<a href="#">More</a>}
      style={{
        width: 750,
      }}
    >
      <p>{props.content}</p>
    </Card>

  </>
);

export default App;