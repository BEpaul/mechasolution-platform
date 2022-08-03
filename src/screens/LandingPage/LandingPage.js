import React, { useState, useEffect, useMemo } from 'react';
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import axios from 'axios';
import TableInterest from '../../components/commons/TableInterest';
import dummy from '../../assets/dummy';
import { dummyDataObject } from '../../assets/dummyDataObject';
import { Button } from 'antd';

// import { SearchOutlined } from '@ant-design/icons';
// import { Button, Tooltip } from 'antd';
// import { AudioOutlined } from '@ant-design/icons';
// import { Input, Space } from 'antd';

// const { Search } = Input;

function LandingPage() {

  const [influencerName, setInfluencerName] = useState('');

  const onInfluencerNameHandler = (event) => {
    setInfluencerName(event.target.value);
  }

  const [dataset, setDataset] = useState([]);

  // 숨기기 보이기
  const [visible, setvisible] = useState(false)

  // 렌더링 최초에 한번만 실행
  // useMemo(() => {
  // }
  //   , [])

  const onClickHandler = (event) => {
    event.preventDefault();
    console.log('입력값', influencerName);
    // 밑으로 이동 예정
    setvisible(true);


    // 계정명 검색 api
    axios.get(`/api/v1/influencerList/search/${influencerName}`)
      .then(response => {
        if (response.data) {

        } else {

        }
      })
  }

  // effect가 발생하는 순간 (버튼 이벤트는 갠춘)
  useEffect(() => {
    const dummyData = dummy.map((item) => {

      setDataset(dataset, [item])
      console.log('아이템', item);

      // return item;
    })
    console.log('데이터셋', dataset);
    console.log('더미데이터', dummyData);

    console.log(dummy)
    return () => {

    }
  })


  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{ textAlign: 'center' }}>
            <h3>안녕하세요, 인플루언서를 위한 공간입니다.</h3>
          </div>
          <br />
          <div>
            <form style={{ display: 'flex', flexDirection: 'row' }}>
              <input type="text" style={{ width: 500, height: 40}}
                value={influencerName}
                placeholder="원하는 계정의 ID를 검색해보세요."
                onChange={onInfluencerNameHandler} />
              {/* <Tooltip title="search">
                <Button shape="circle" icon={<SearchOutlined />} size="large" onClick={onClickHandler}/>
              </Tooltip> */}
              <Button type='primary' onClick={onClickHandler} style={{ height: 40 }}>검색</Button>
            </form>
          </div>
          <br />
          <div>
            {visible && <TableInterest data={dummyDataObject} />}
          </div>
        </MainHeader>
      </Header>
    </Container>
  )
}

export default LandingPage