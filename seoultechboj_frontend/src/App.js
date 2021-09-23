import React from 'react';
import Home from './components/Home';
import Header from './components/Header';
import Footer from './components/Footer';
import ProblemList from './components/problem/ProblemList';
import {BrowserRouter, Route} from 'react-router-dom';



function App() {
  return (
    <BrowserRouter>
      <Header/>
        <Route exact path="/home" component={Home} />
        <Route path="/problem" component={ProblemList} />
      <Footer/>
    </BrowserRouter>
  );
}

export default App;
