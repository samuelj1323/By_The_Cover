import React from "react";
import Carousel from "../components/Carousel"

//images:
import rev from "../assets/revenant.png"
import sw from "../assets/Star-Wars-Movie-Poster.jpeg"
import b2f from "../assets/b2f.jpeg"
import FN from "../assets/FN.jpg"
class RecPage extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            title:"By The Cover",
            items:[
                    {
                        id:1,
                        title:"Revenant",
                        genre:"Gritty",
                        year:"2016",
                        image_path: rev,
                    },
                    {
                        id:2,
                        title:"Star Wars",
                        genre:"sci-fy",
                        year:"1986",
                        image_path: sw,
                    },
                    {
                        id:3,
                        title:"Back to the Future",
                        genre:"Kids",
                        year:"2010",
                        image_path: b2f,
                    },
                    {
                        id:4,
                        title:"Finding Nemo",
                        genre:"Kids",
                        year:"2003",
                        image_path:FN,
                    },
                    {
                        id:5,
                        title:"Bugs Life",
                        genre:"Kids",
                        year:"1998",
                        image_path: rev,
                    },
                    {
                        id:6,
                        title:"AirBud",
                        genre:"Kids",
                        year:"1998",
                        image_path: rev,
                  },
                  {
                    id:1,
                    title:"Toy Story",
                    genre:"Kids",
                    year:"1995",
                    image_path: rev,
                },
                {
                    id:2,
                    title:"Toy Story2",
                    genre:"Kids",
                    year:"1999",
                    image_path: rev,
                },
                {
                    id:3,
                    title:"Toy Story3",
                    genre:"Kids",
                    year:"2010",
                    image_path: rev,
                },
                {
                    id:4,
                    title:"Finding Nemo",
                    genre:"Kids",
                    year:"2003",
                    image_path:rev,
                },
                {
                    id:5,
                    title:"Bugs Life",
                    genre:"Kids",
                    year:"1998",
                    image_path: rev,
                },
                {
                    id:6,
                    title:"AirBud",
                    genre:"Kids",
                    year:"1998",
                    image_path: rev,
              },{
                      id:1,
                      title:"Captain America",
                      genre:"Fantasy",
                      year:"2010",
                      image_path: rev,
                  },
                  {
                      id:2,
                      title:"Avengers",
                      genre:"Sci-Fy",
                      year:"2012",
                      image_path: rev,
                  },
                  {
                      id:3,
                      title:"Brave Heart",
                      genre:"Action",
                      year:"2005",
                      image_path: rev,
                  },
                  {
                      id:4,
                      title:"Thor",
                      genre:"Fantasy",
                      year:"2008",
                      image_path: rev,
                  },
                  {
                      id:5,
                      title:"Superman",
                      genre:"Fantasy",
                      year:"2014",
                      image_path: rev,
                  },
                  {
                      id:6,
                      title:"Dark Knight",
                      genre:"Sci-fy",
                      year:"2016",
                      image_path: rev,
                },
              ],
          };
    }
    render(){
        return(
            <div className="body">
                <h1 className="header" style={{fontSize:56, flex:1}}> By The Cover</h1>
                <h2 style={{color:"white"}}>Most Similar to the Poster art...</h2>
                <Carousel movies={this.state.items}/>
                <h2 style={{color:"white"}}>Most Similar to the Musical Score...</h2>
                <Carousel movies={this.state.items}/>
                <h2 style={{color:"white"}}>Most Similar to the Musical Score...</h2>
                <Carousel movies={this.state.items}/>
                <h2 style={{color:"white"}}>Most Similar to both Poster Art and Musical Score...</h2>
                <Carousel movies={this.state.items}/>
                <h2 style={{color:"white"}}>Least Similar to Poster art...</h2>
                <Carousel movies={this.state.items}/>
                <h2 style={{color:"white"}}>Least Similar to Musical Score...</h2>
                <Carousel movies={this.state.items}/>
            </div>
        );
    }
}
export default RecPage;