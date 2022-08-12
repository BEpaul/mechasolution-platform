import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import TableInterest from '../../components/tables/TableInterest';
import { Button } from 'antd';
import APICollection from '../../api/APICollection';
import ImageBox from '../../components/commons/ImageBox'

function LandingPage() {

  let APICol = new APICollection();

  const navigate = useNavigate();

  const [influencerName, setInfluencerName] = useState('');

  const onInfluencerNameHandler = (event) => {
    setInfluencerName(event.target.value);
  }

  // api 데이터
  // const [data, setData] = useState([])

  const onClickHandler = (event) => {
    event.preventDefault();
    console.log('입력값', influencerName);

    navigate('/influencer', {
      state : {
        influencerName: influencerName,
      },
    });
  }

  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{ textAlign: 'center' }}>
            <h3>안녕하세요, 인플루언서를 위한 공간입니다.</h3>
            <h4>원하는 계정명을 검색해 확인해보세요!</h4>
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
          {/* <div> */}
          <ImageBox />
          {/* {visible && <TableInterest data={data} isLoginCheck={true} />} */}
          {/* </div> */}
        </MainHeader>
      </Header>
    </Container>
  )
}

export default LandingPage