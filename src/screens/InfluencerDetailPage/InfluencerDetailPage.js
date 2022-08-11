import React, { useState, useEffect } from 'react'
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import { Body, MainBody } from '../../components/styles/body/Body.styled';
import { UserOutlined } from '@ant-design/icons';
import { Avatar, Row, Col } from 'antd';
import GridCards from '../../components/commons/GridCards';
import RankingChart from '../../components/charts/RankingChart';
import PowerChart from '../../components/charts/PowerChart';
import { dumDataRankingChart } from '../../assets/dumDataRankingChart';
import { useLocation } from 'react-router-dom';
import APICollection from '../../api/APICollection';
import './styles.css';


function InfluencerDetailPage() {

  let APICol = new APICollection();
  const [data, setData] = useState([]);
  
  // 랜딩페이지로부터 입력값 전달받기
  const fromLanding = useLocation();
  const influencerName = fromLanding.state.influencerName;
  console.log('받은 인플루언서 이름', influencerName);
  
  useEffect(() => {
      // 전달 받은 입력값으로 서버에 요청
    APICol.SearchName(influencerName).then((response) => {
      console.log(response.data);
      setData(response.data)
    })
  }, [])


  
  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <Avatar size={90} icon={<UserOutlined />} />
            <h4 style={{ padding: 20 }}>{data.influencer}의 분석리포트</h4>
          </div>
          <br />
          <h5>카테고리: {data.category}</h5>
          <h5>팔로워: {data.follower}</h5>
          <h5>영향력: {data.power}</h5>
          <br />
          <Row>
            <Col>
            </Col>
          </Row>
        </MainHeader>
      </Header>
      <Body>
        <MainBody>
          <Row>
            <Col span={11}>
              <GridCards title='내 랭킹' content={<RankingChart data={dumDataRankingChart} />} />
            </Col>
            <Col span={2} />
            <Col span={11}>
              <GridCards title='내 영향력' content={<PowerChart data={data}/>} />
            </Col>
          </Row>
        </MainBody>
      </Body>
    </Container>
  )
}

export default InfluencerDetailPage