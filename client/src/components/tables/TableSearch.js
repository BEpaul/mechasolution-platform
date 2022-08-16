import { Space, Table, Button } from 'antd';
import axios from 'axios';
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
    title: '인플루언서 관리',
    key: 'action',
    align: 'center',
    render: (_, record) => (
      <Space size="middle">
        <Button 
        type='primary' 
        key={columns[0].key}
        onClick={()=> {
            console.log('키', record.Username);
            axios.post(`http://localhost:8000/api/v1/attention/${record.Username}`)
            .then(response => {
              console.log('메세지',response.data);

              if(response.data.detail == 'Attention list is full.'){
                alert('담을 수 있는 인플루언서는 최대 5인입니다.')
              }
              else if(response.data.detail == 'Already added.'){
                alert('이미 폴더에 있는 인플루언서입니다.')
              }
              else{
                alert('저장되었습니다.');
              }
            })

            
        }}
        >
          저장하기
        </Button>
      </Space>
    ),
  },
];

const App = (props) => <Table style={{ width: 800}} columns={columns} dataSource={props.data} pagination={{ pageSize: 5, pageSizeOptions: [5, 10, 20] }} />;

export default App;