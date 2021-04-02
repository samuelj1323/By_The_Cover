
import './App.css';
import React from 'react';
//Pages:
import RecPage from "./pages/RecPage.js"; // Recommender Page
import InputPage from "./pages/InputPage.js"; //Input Page
class App extends React.Component{
  constructor(props){
    super(props);
  }
  render(){
    return(
      <div>
        <RecPage/>
        
      </div>
      

    )
  }
}

export default App;
