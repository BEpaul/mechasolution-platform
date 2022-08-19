import './App.css';
import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import LandingPage from './screens/LandingPage/LandingPage';
import InterestPage from './screens/InterestPage/InterestPage';
import RankingPage from './screens/RankingPage/RankingPage';
import LoginPage from './screens/LoginPage/LoginPage';
import RegisterPage from './screens/RegisterPage/RegisterPage';
import SearchPage from './screens/SearchPage/SearchPage';
import InfluencerDetailPage from './screens/InfluencerDetailPage/InfluencerDetailPage';
import NavBar from './components/views/NavBar/NavBar';
import Footer from './components/views/Footer/Footer';
// import 'bootstrap/dist/css/bootstrap.min.css';
import 'antd/dist/antd.min.css';


function App() {
  return (
    <Router>
      <NavBar />
      <div>
        <Routes>
          <Route exact path="/" element = {<LandingPage />} />
          <Route exact path="/interest" element = {<InterestPage />} />
          <Route exact path="/ranking" element = {<RankingPage />} />
          <Route exact path="/search" element = {<SearchPage />} />
          <Route exact path="/login" element = {<LoginPage />} />
          <Route exact path="/register" element = {<RegisterPage />} />
          <Route exact path="/influencer" element = {<InfluencerDetailPage />} />
        </Routes>
      </div>
      <Footer />
    </Router>
  );
}

export default App;