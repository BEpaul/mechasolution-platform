import React from 'react'
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import { Body, MainBody } from '../../components/styles/body/Body.styled';
import { UserOutlined } from '@ant-design/icons';
import { Avatar, Row, Col } from 'antd';
import GridCards from '../../components/commons/GridCards';
import RankingChart from '../../components/charts/RankingChart';
import PowerChart from '../../components/charts/PowerChart';
import { dumDataRankingChart } from '../../assets/dumDataRankingChart';
import './styles.css';


function InfluencerDetailPage() {
  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <Avatar size={90} icon={<UserOutlined />} />
            <h4 style={{ padding: 20 }}>@username의 분석리포트</h4>
          </div>
          <br />
          <h5>게시글: 132개</h5>
          <h5>팔로워: 4,021명</h5>
          <h5>팔로잉: 96명</h5>
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
              <GridCards title='내 영향력' content={<PowerChart />} />
            </Col>
          </Row>
        </MainBody>
      </Body>
    </Container>
  )
}

export default InfluencerDetailPage