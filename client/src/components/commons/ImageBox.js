import { Image } from 'antd';
import React from 'react';
import img from '../../assets/mainimg.png'

const App = () => (
  <Image
    width={650}
    height={400}
    style={{ padding: 10}}
    src={img}
    />
);

export default App;