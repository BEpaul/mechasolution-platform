import { Select } from 'antd';
import React from 'react';
const { Option } = Select;

  const App = (props) => (
    <>
      <Select
        defaultValue={props.defaultValue}
        style={{
          width: 150,
          margin: 20,
        }}
        onChange={props.onChange}
      >
        <Option value=''>{props.defaultValue}</Option>        
        <Option value='all'>{props.option1}</Option>
        <Option value='nano'>{props.option2}</Option>
        <Option value='micro'>{props.option3}</Option>
        <Option value='mid'>{props.option4}</Option>
        <Option value='macro'>{props.option5}</Option>
        <Option value='mega'>{props.option6}</Option>
      </Select>
    </>
  );
  
  export default App;