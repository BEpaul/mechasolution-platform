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
    width: 150,
  },
  {
    title: '인플루언서 연결',
    key: 'action',
    align: 'center',
    width: 150,
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