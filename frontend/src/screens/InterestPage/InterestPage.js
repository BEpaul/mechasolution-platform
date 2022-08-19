import React, { useEffect, useState }from 'react'
import TableInterest from '../../components/tables/TableInterest'
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import { dummyDataObject } from '../../assets/dummyDataObject';
import APICollection from '../../api/APICollection';

function InterestPage() {

  let APICol = new APICollection();

  const [data, setData] = useState()
  useEffect(() => {
    APICol.AttentionList().then(response => {
      console.log(response.data);
      setData(response.data);
    })
  }, [])

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
                <TableInterest data={data} style={{width: 800}} />
              </div>
          </MainHeader>
        </Header>
      </Container>
    </div>
  )
}

export default InterestPage