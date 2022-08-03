/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react';
import { Menu } from 'antd';

function RightMenu() {
  return (
    <Menu mode='horizontal'>
      <Menu.Item key="mail">
        <a href="/login">로그인</a>
      </Menu.Item>
      <Menu.Item key="app">
        <a href="/register">회원가입</a>
      </Menu.Item>
    </Menu>
  )
}



export default RightMenu;

