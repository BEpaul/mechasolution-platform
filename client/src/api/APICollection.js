import axios from 'axios'

class APICollection {

  // 테스트
  SearchTest(){ return axios.get(`http://localhost:8000/api/v1/influencers`);}

  // 상세보기 페이지에서 인플루언서 계정 검색
  // SearchName(influencerName){ return axios.get(`http://localhost:8000/api/v1/influencers/${influencerName}`);}
  // SearchName(influencerName){ return axios.get(`http://192.168.0.15:5000/api/v1/influencers/search/user/${influencerName}`);}
  SearchName(influencerName){ return axios.get(`http://localhost:8000/api/v1/influencers/search/user/${influencerName}`);}

  // 해시태그 && 키워드 검색 api
  SearchKeyword(Keyword) { return axios.get(`http://localhost:8000/api/v1/influencers/search/${Keyword}`);}

  // 검색페이지 하단 카테고리 리스트
  CategoryRanking(Category) { return axios.get(`http://localhost:8000/api/v1/influencers/rank/${Category}`)}

  // 페이징 처리
  

  // 관심 인플루언서 목록
  AttentionList() {
    return axios.get(`http://localhost:8000/api/v1/attention`);
  }


}

export default APICollection

