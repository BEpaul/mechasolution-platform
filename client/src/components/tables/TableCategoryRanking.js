import { Table } from 'antd';
import React from 'react';
const columns = [
  {
    title: '인플루언서',
    dataIndex: 'influencer',
    key: 'influencer',
    align: 'center',
    render: (text) => <div>{text}</div>,
  },
  {
    title: '팔로워 수',
    dataIndex: 'follower',
    key: 'follower',
    align: 'center',
  },
  {
    title: '영향력',
    key: 'power',
    dataIndex: 'power',
    align: 'center',
  },
];

const App = (props) => <Table columns={columns} dataSource={props.data} />;

export default App;