
import './App.css';
import React from 'react';
//Pages:
//import RecPage from "./pages/RecPage.js"; // Recommender Page
import InputPage from "./pages/InputPage.js"; //Input Page
//import {Navbar, Nav} from 'react-bootstrap'
//import {HashRouter as Router, Route, Link} from 'react-router-dom'
class App extends React.Component{
  constructor(props){
    super(props);
  }
  render(){
    return(
     <InputPage/>
      

    )
  }
}

export default App;
