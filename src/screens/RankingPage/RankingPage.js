import TableCategoryRanking from '../../components/tables/TableCategoryRanking';
import TableSearch from '../../components/tables/TableSearch';
import React, { useState } from 'react';
import GridCards from '../../components/commons/GridCards';
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import { Body, MainBody } from '../../components/styles/body/Body.styled';
import { dummyDataObject } from '../../assets/dummyDataObject';
import { Button, Col, Row } from 'antd';

import axios from 'axios';

function RankingPage() {

  const [Keyword, setKeyword] = useState('');

  const onKeywordHandler = (event) => {
    setKeyword(event.target.value);
  }

  const [visible, setvisible] = useState(false);
  
  const onClickHandler = (event) => {
    event.preventDefault();
    setvisible(true);
    console.log('입력값', Keyword)

    // 해시태그 && 키워드 검색 api
    axios.get(`/api/v1/influencerList/search/${Keyword}`)
    .then(response => {
      if(response.data){

      } else {

      }
    })
  }

  // 인스타그램 캠핑, 골프 카테고리 순위 api

  axios.get(`/api/v1/influencerList/camping`)
  .then(response => {
    if(response.data){

    } else {

    }
  })

  axios.get(`/api/v1/influencerList/golf`)
  .then(response => {
    if(response.data){

    } else {

    }
  })


  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{textAlign: 'center'}}>
            <h3>랭킹을 확인하고자 하는 계정을 검색해보세요!</h3>
            <br />
            <form style={{ display: 'flex', justifyContent: 'center' }}>
              <input type="text" style={{ width: 500, height: 40}} value={Keyword} placeholder="해시태그 및 키워드를 검색하세요." onChange={onKeywordHandler} />
              <Button type='primary' onClick={onClickHandler} style={{ height: 40 }} >검색</Button>
            </form>
          </div>
          <br />
          {/* 각 카테고리별 인플루언서 랭킹 그리드뷰 */}
          {visible && <TableSearch data={dummyDataObject} />}
          <div>

          </div>
        </MainHeader>
      </Header>
      <Body>
        <MainBody>
        <Body>
        <MainBody>
          <Row>
            <Col span={11}>
              <GridCards title='인스타그램 캠핑 카테고리' content={<TableCategoryRanking data={dummyDataObject}/>}/>
            </Col>
            <Col span={2} />
            <Col span={11}>
            <GridCards title='인스타그램 골프 카테고리' content={<TableCategoryRanking data={dummyDataObject}/>}/>
            </Col>
          </Row>
        </MainBody>
      </Body>
        </MainBody>
      </Body>
    </Container>
  )
}

export default RankingPage