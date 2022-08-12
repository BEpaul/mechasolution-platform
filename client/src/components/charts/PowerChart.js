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
    category: "캠핑",
    power: 4000,
  },
  {
    category: "골프",
    power: 3000,
  },
  {
    category: "패션",
    power: 2000,
  },
  {
    category: "음식",
    power: 2780,
  },
  {
    category: "축구",
    power: 1890,
  },
  {
    category: "IT",
    power: 2390,
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
      <XAxis dataKey="category" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Bar dataKey="power" fill="#82ca9d" />
    </BarChart>
  );
}