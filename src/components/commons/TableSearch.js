import { Space, Table, Button } from 'antd';
import React from 'react';
const columns = [
  {
    title: '인플루언서',
    dataIndex: 'influencer',
    key: 'influencer',
    render: (text) => <div>{text}</div>,
  },
  {
    title: '카테고리',
    dataIndex: 'category',
    key: 'category',
  },
  {
    title: '팔로워 수',
    dataIndex: 'follower',
    key: 'follower',
  },
  {
    title: '영향력',
    key: 'power',
    dataIndex: 'power',
  },
  {
    title: '인플루언서 관리',
    key: 'action',
    render: (_, record) => (
      <Space size="middle">
        <div></div>
        <Button type='primary'>저장하기</Button>
      </Space>
    ),
  },
];

const App = (props) => <Table style={{ textAlign: 'center'}} columns={columns} dataSource={props.data} />;

export default App;