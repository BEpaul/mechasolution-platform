import React, { useState } from 'react';
import { Container } from '../../components/styles/container/Container';
import { Header, MainHeader } from '../../components/styles/header/Header.styled';
import SelectBox from '../../components/commons/SelectBox';
import SelectBoxCategory from '../../components/commons/SelectBoxCategory'
import { Button } from 'antd';
import TableSearch from '../../components/tables/TableSearch';
import axios from 'axios';

function SearchPage() {

  const [OptionFollowerValue, setOptionFollowerValue] = useState('')
  const [OptionCategoryValue, setOptionCategoryValue] = useState('')

  const [data, setData] = useState([])

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

    // 필터링 api 메소드
    axios.get(`http://localhost:8000/api/v1/influencers/rank/${OptionFollowerValue}/${OptionCategoryValue}`
    // {
    //   params: {
    //     followers: OptionFollowerValue,
    //     category: OptionCategoryValue,
    //   }
    // }
    ).then(response => {
      console.log(response.data);
      setData(response.data);
    }).catch(error => {
      console.log(error.response);
    })

    // 카테고리별 순위 리스트
    // Category(category) { return axios.post(`/api/v1/influencers/${category}`)}

    // CategoryCamping(){ return axios.get(`/api/v1/category/camping`)};

    // CategoryGolf(){ return axios.get(`/api/v1/category/golf`)};
  }

  return (
    <Container>
      <Header>
        <MainHeader>
          <div style={{ textAlign: 'center' }}>
            <h3>필터를 이용해서 인플루언서의 순위를 확인해보세요.</h3>
          </div>
          <div style={{ padding: 15, textAlign: 'center' }}>
            <SelectBox
              defaultValue='팔로워 수'
              option1='제한 없음'
              option2='1K ~ 10K'
              option3='10K ~ 50K'
              option4='50K ~ 100K'
              option5='100K ~ 500K'
              option6='500K ~'
              onChange={handleFollowerChange}
            />
            <SelectBoxCategory
              defaultValue='카테고리'
              option1='골프'
              option2='조명'
              option3='캠핑'
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
            <TableSearch data={data} />
          </div>
        </MainHeader>

      </Header>
    </Container>
  )
}

export default SearchPage