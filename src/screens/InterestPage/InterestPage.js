import React from 'react'
import TableInterest from '../../components/tables/TableInterest'
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import { dummyDataObject } from '../../assets/dummyDataObject';

function InterestPage() {
  return (
    <div>
      <Container>
        <Header>
          <MainHeader>
              <div style={{padding: 10, textAlign: 'center'}}>
                <h3>관심있는 인플루언서를 관리할 수 있습니다.</h3>
              </div>
              <br />
              <div>
                <TableInterest data={dummyDataObject} style={{width: 800}} />
              </div>
          </MainHeader>
        </Header>
      </Container>
    </div>
  )
}

export default InterestPage