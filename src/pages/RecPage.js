import React from "react";
import Carousel from "../components/Carousel"
//import Button from 'react-bootstrap/Button'
//import {Link} from 'react-router-dom'
//images:
//import rev from "../assets/revenant.png"
//import sw from "../assets/Star-Wars-Movie-Poster.jpeg"
//import b2f from "../assets/b2f.jpeg"
import FN from "../assets/FN.jpg"
class RecPage extends React.Component{
    constructor(props){ // contstructs our information 
        super(props)
        this.state = {
            title:"By The Cover",
            items:[
                {
                    title:'toy movie',
                    genre:'action',
                    year:2002,
                    image:FN
                }
                ]
          };
    }
    
    
    render(){ // displays our beautiful information.
        return(
            <div className="body">
                
                <h2 style={{color:"white"}}>We begin with...</h2>
                <Carousel movies={this.props.original}/>
                <h2 style={{color:"white"}}>Most Similar to the Poster art...</h2>
                <Carousel movies={this.props.movies1}/>
                <h2 style={{color:"white"}}>Least Similar to the Poster art...</h2>
                <Carousel movies={this.props.movies2}/>
                <h2 style={{color:"white"}}>Most Similar to the Musical Score...</h2>
                <Carousel movies={this.props.movies3}/>
                <h2 style={{color:"white"}}>Least Similar to the Musical Score...</h2>
                <Carousel movies={this.props.movies4}/>
                <h2 style={{color:"white"}}>Most Similar with Sound and then Poster art...</h2>
                <Carousel movies={this.props.movies5}/>
                
                
            </div>
        );
    }
}
export default RecPage;