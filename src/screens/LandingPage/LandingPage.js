import React, { useState, useEffect } from 'react';
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import TableInterest from '../../components/tables/TableInterest';
import { Button } from 'antd';
import APICollection from '../../api/APICollection';

function LandingPage() {

  let APICol = new APICollection(); 
  const [influencerName, setInfluencerName] = useState('');

  const onInfluencerNameHandler = (event) => {
    setInfluencerName(event.target.value);
  }

  // 숨기기 보이기
  const [visible, setvisible] = useState(false)
  
  // api 데이터
  const [data, setData] = useState([])

  const onClickHandler = async (event) => {
    event.preventDefault();
    console.log('입력값', influencerName);

    APICol.SearchName(influencerName).then((value) => {
      setData(value.data);
    });

    setvisible(true);
  }

  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{ textAlign: 'center' }}>
            <h3>안녕하세요, 인플루언서를 위한 공간입니다.</h3>
          </div>
          <br />
          <div>
            <form style={{ textAlign: 'center' }}>
              <input type="text" style={{ width: 500, height: 40 }}
                value={influencerName}
                placeholder="원하는 계정의 이름을 검색해보세요."
                onChange={onInfluencerNameHandler} />
              <Button type='primary' onClick={onClickHandler} style={{ height: 40 }}>검색</Button>
            </form>
          </div>
          <br />
          <div>
            {visible && <TableInterest data={data} isLoginCheck={true} />}
          </div>
        </MainHeader>
      </Header>
    </Container>
  )
}

export default LandingPage