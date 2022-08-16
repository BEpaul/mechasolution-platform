import "./ChartStyles.css";
import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";

const data = [
  {
    name: "패션",
    평균: 4000,
    "내 영향력": 2400,
    amt: 2400
  },
  {
    name: "캠핑",
    평균: 3000,
    "내 영향력": 1398,
    amt: 2210
  },
  {
    name: "IT",
    평균: 2000,
    "내 영향력": 9800,
    amt: 2290
  },
  {
    name: "헬스",
    평균: 2780,
    "내 영향력": 3908,
    amt: 2000
  },
  {
    name: "골프",
    평균: 1890,
    "내 영향력": 4800,
    amt: 2181
  },

];

export default function App() {


  return (
    <BarChart
      width={650}
      height={400}
      data={data}
      margin={{
        top: 5,
        right: 0,
        left: 0,
        bottom: 5
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Bar dataKey="내 영향력" fill="#8884d8" />
      <Bar dataKey="평균" fill="#82ca9d" />
    </BarChart>
  );
}
