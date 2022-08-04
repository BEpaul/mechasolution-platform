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
    name: "캠핑",
    영향력: 4000,
    활동량: 2400,
    amt: 2400
  },
  {
    name: "골프",
    영향력: 3000,
    활동량: 1398,
    amt: 2210
  },
  {
    name: "패션",
    영향력: 2000,
    활동량: 9800,
    amt: 2290
  },
  {
    name: "음식",
    영향력: 2780,
    활동량: 3908,
    amt: 2000
  },
  {
    name: "축구",
    영향력: 1890,
    활동량: 4800,
    amt: 2181
  },
  {
    name: "IT",
    영향력: 2390,
    활동량: 3800,
    amt: 2500
  }
];

export default function App() {
  return (
    <BarChart
      width={650}
      height={350}
      data={data}
      margin={{
        top: 5,
        right: 0,
        left: 0,
        bottom: 0
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Bar dataKey="활동량" fill="#8884d8" />
      <Bar dataKey="영향력" fill="#82ca9d" />
    </BarChart>
  );
}