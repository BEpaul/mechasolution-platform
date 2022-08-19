import { Table } from 'antd';
import React from 'react';
const columns = [
  {
    title: '순위',
    dataIndex: 'Rank',
    key: 'Rank',
    align: 'center',
  },
  {
    title: '인플루언서',
    dataIndex: 'Username',
    key: 'Username',
    align: 'center',
    render: (text) => <div>{text}</div>,
  },
  {
    title: '팔로워 수',
    dataIndex: 'Followers',
    key: 'Followers',
    align: 'center',
  },
  {
    title: '영향력',
    key: 'Real_Influence',
    dataIndex: 'Real_Influence',
    align: 'center',
  },
];

const App = (props) => <Table columns={columns} dataSource={props.data} pagination={{ hideOnSinglePage : true }} />;

export default App;