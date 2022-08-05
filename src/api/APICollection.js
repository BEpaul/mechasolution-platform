import axios from 'axios'

class APICollection {

  // 테스트
  SearchTest(){ return axios.get(`http://localhost:8000/api/v1/influencers`);}

  // 랜딩페이지에서 인플루언서 계정 검색
  SearchName(influencerName){ return axios.get(`http://localhost:8000/api/v1/influencers/${influencerName}`);}

  // 해시태그 && 키워드 검색 api
  SearchKeyword(Keyword) { axios.get(`/api/v1/influencerList/search/${Keyword}`);}

  // 카테고리별 순위 리스트
  CategoryCamping(){ return axios.get(`/api/v1/category/camping`)};

  CategoryGolf(){ return axios.get(`/api/v1/category/golf`)};

  // 페이징 처리

  // 인플루언서 담기(찜)
  Save() {
    return axios.post(``);
  }

  // 관심 인플루언서 목록
  AttentionList() {
    return axios.get(``);
  }

  // 관심 인플루언서 삭제
  AttentionDelete() {
    return axios.delete(``);
  }

  // 

}

export default APICollection

