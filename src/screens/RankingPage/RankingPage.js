import React, { useState } from 'react';
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import SelectBox from '../../components/commons/SelectBox';
import { Button } from 'antd';
import TableSearch from '../../components/tables/TableSearch'
import { dummyDataObject } from '../../assets/dummyDataObject';

function SearchPage() {

  const [OptionFollowerValue, setOptionFollowerValue] = useState('')
  const [OptionCategoryValue, setOptionCategoryValue] = useState('')

  const handleFollowerChange = (value) => {
    console.log(`selected ${value}`);
    setOptionFollowerValue(value);
  };

  const handleCategoryChange = (value) => {
    console.log(`selected ${value}`);
    setOptionCategoryValue(value);
  }


  const onClickHandler = (event) => {
    event.preventDefault();
    console.log("팔로워 옵션", OptionFollowerValue);
    console.log("카테고리 옵션", OptionCategoryValue);
    
  }

  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{textAlign: 'center'}}>
            <h3>필터를 이용해서 인플루언서의 순위를 확인해보세요.</h3>
          </div>
          <div style={{ padding: 15, textAlign: 'center'}}>
            <SelectBox
              defaultValue='팔로워 수'
              option1='0 ~ 10k'
              option2='10k ~ 50k'
              option3='50k ~ 100k'
              onChange={handleFollowerChange}
            />
            <SelectBox
              defaultValue='카테고리'
              option1='연예'
              option2='역사'
              option3='음식'
              onChange={handleCategoryChange}
            />

            <Button
              type='primary'
              style={{
                margin: 20,
                width: 120
              }}
              onClick={onClickHandler}
            >
              필터링 적용
            </Button>
          </div>

          <div>
            <TableSearch data={dummyDataObject} />
          </div>
        </MainHeader>

      </Header>
    </Container>
  )
}

export default SearchPage