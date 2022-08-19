import TableCategoryRanking from '../../components/tables/TableCategoryRanking';
import TableSearch from '../../components/tables/TableSearch';
import React, { useState, useEffect } from 'react';
import GridCards from '../../components/commons/GridCards';
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import { Body, MainBody } from '../../components/styles/body/Body.styled';
import { Button, Col, Row } from 'antd';
import APICollection from '../../api/APICollection';

function RankingPage() {

  let APICol = new APICollection();

  const [Keyword, setKeyword] = useState('');

  // 랭킹 검색 데이터
  const [data, setData] = useState([]);

  // 캠핑 카테고리 데이터
  const [campingData, setCampingData] = useState([])

  // 골프 카테고리 데이터 데이터
  const [golfData, setGolfData] = useState([])

  const onKeywordHandler = (event) => {
    setKeyword(event.target.value);
  }

  const [visible, setvisible] = useState(false);

  // 랭킹페이지 렌더링 시 카테고리별 랭킹
  useEffect(() => {
    APICol.CategoryRanking('light').then((response) => {
      console.log(response.data);
      setCampingData(response.data);

    APICol.CategoryRanking('golf').then((response) => {
      console.log(response.data);
      setGolfData(response.data);
    })

    })
  }, [])
  


  const onClickHandler = (event) => {
    event.preventDefault();
    console.log('입력값', Keyword);

    // 키워드에 빈값을 넣었을 때
    // if(event.target.value === '') {
    //   alert('값을 입력해주세요.');
    //   window.location.replace('/search');
    // }

    // 해시태그 및 키워드 검색
    APICol.SearchKeyword(Keyword).then((response) => {
      console.log(response.data);
      setData(response.data);
      setvisible(true);
    }).catch(error => {
      console(error.response);
    });
  }

  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{ textAlign: 'center' }}>
            <h3>관심있는 분야나 키워드를 검색해보세요!</h3>
            <br />
            <form style={{ display: 'flex', justifyContent: 'center' }}>
              <input type="text" style={{ width: 500, height: 40 }} value={Keyword} placeholder="해시태그 및 키워드를 검색하세요." onChange={onKeywordHandler} />
              <Button type='primary' onClick={onClickHandler} style={{ height: 40 }} >검색</Button>
            </form>
          </div>
          <br />
          {/* 각 카테고리별 인플루언서 랭킹 그리드뷰 */}
          {visible && <TableSearch data={data} />}
        </MainHeader>
      </Header>
      <Body>
        <MainBody>
          <Row>
            <Col span={11}>
              <GridCards title='인스타그램 캠핑 카테고리' content={<TableCategoryRanking data={campingData} />} />
            </Col>
            <Col span={2} />
            <Col span={11}>
              <GridCards title='인스타그램 골프 카테고리' content={<TableCategoryRanking data={golfData} />} />
            </Col>
          </Row>
        </MainBody>
      </Body>
    </Container>
  )
}

export default RankingPage