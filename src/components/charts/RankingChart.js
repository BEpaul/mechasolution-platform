import "./ChartStyles.css";
import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";

const data = [
  {
    name: "21-01",
    uv: 4000,
    pv: 2400,
    amt: 2400
  },
  {
    name: "21-04",
    uv: 3000,
    pv: 1398,
    amt: 2210
  },
  {
    name: "21-07",
    uv: 2000,
    pv: 9800,
    amt: 2290
  },
  {
    name: "21-10",
    uv: 2780,
    pv: 3908,
    amt: 2000
  },
  {
    name: "22-01",
    uv: 1890,
    pv: 4800,
    amt: 2181
  },
  {
    name: "22-04",
    uv: 2390,
    pv: 3800,
    amt: 2500
  },
  {
    name: "22-07",
    uv: 3490,
    pv: 4300,
    amt: 2100
  }
];

export default function App(props) {
  return (
    <LineChart
      width={650}
      height={350}
      data={props.data}
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
      <Line
        type="monotone"
        dataKey="pv"
        stroke="#8884d8"
        activeDot={{ r: 8 }}
      />
      <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
    </LineChart>
  );
}