import { Button } from 'antd';
import { Space, Table } from 'antd';
import axios from 'axios';
import React from 'react';

const columns = [
  {
    title: '인플루언서',
    dataIndex: 'Influencer_id',
    key: 'Influencer_id',
    align: 'center',
    render: (text) => <a>{text}</a>,
  },
  {
    title: '카테고리',
    dataIndex: 'Category',
    key: 'Category',
    align: 'center',
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
    width: 150,
  },
  {
    title: '인플루언서 관리',
    key: 'action',
    align: 'center',
    width: 150,
    render: (_, record) => (
      <Space size="middle">
        <Button 
        type='primary'
        onClick={() => {
          axios.delete(`http://localhost:8000/api/v1/attention/${record.Influencer_id}`)
          alert('삭제되었습니다');
          window.location.replace('/interest');
        }}
         >
          삭제
        </Button>
      </Space>
    ),
  },
  {
    title: '인플루언서 연결',
    key: 'action',
    align: 'center',
    width: 150,
    render: (_, record) => (
      <Space size="middle">
        <Button 
        type='primary'
        onClick={() => {
          alert('서비스 준비중입니다.');
        }}
         >
          DM
        </Button>
      </Space>
    ),
  },
];

const App = (props) => <Table columns={columns} dataSource={props.data} style={{width: 800}} pagination={{ pageSize: 5 }} />;

export default App;