import React from 'react';
import { Menu } from 'antd';

function LeftMenu(props) {
  return (
    <Menu mode={props.mode}>
    <Menu.Item key="mail">
      <a href="/">홈</a>
    </Menu.Item>
    <Menu.Item key="ranking">
      <a href="/ranking">인플루언서 랭킹</a>
    </Menu.Item>
    <Menu.Item key="search">
      <a href="/search">인플루언서 검색</a>
    </Menu.Item>
    <Menu.Item key="interest">
      <a href="/interest">내 관심 인플루언서</a>
    </Menu.Item>
  </Menu>
  )
}

export default LeftMenu