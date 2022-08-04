import axios from 'axios'



class APICollection {

  // 테스트
  SearchTest(){ return axios.get(`http://localhost:8000/api/v1/influencers`);}

  // 랜딩페이지에서 인플루언서 계정 검색
  SearchName(influencerName){ return axios.get(`http://localhost:8000/api/v1/${influencerName}`);}

  // 해시태그 및 키워드 검색

  // 카테고리별 순위 리스트
  categoryCamping(){ return axios.get(`/api/v1/category/camping`)};

  categoryGolf(){ return axios.get(`/api/v1/category/golf`)};

  


}
export default APICollection

