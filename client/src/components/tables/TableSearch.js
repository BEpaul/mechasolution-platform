import { Space, Table, Button } from 'antd';
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
    title: '카테고리',
    dataIndex: 'category',
    key: 'category',
    align: 'center',
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
  {
    title: '인플루언서 관리',
    key: 'action',
    align: 'center',
    render: (_, record) => (
      <Space size="middle">
        <div></div>
        <Button type='primary' key={columns[0].key}>저장하기</Button>
      </Space>
    ),
  },
];

const App = (props) => <Table style={{ textAlign: 'center', width: 800}} columns={columns} dataSource={props.data} />;

export default App;