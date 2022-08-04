import { Button } from 'antd';
import { Space, Table } from 'antd';
import React from 'react';

const loginCheck = () => {

}
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
    title: '인플루언서 연결',
    key: 'action',
    render: (_, record) => (
      <Space size="middle">
        <div></div>
        <Button type='primary' >DM</Button>
      </Space>
    ),
  },
];

const App = (props) => <Table columns={columns} dataSource={props.data} style={{width: 800}} />;

export default App;