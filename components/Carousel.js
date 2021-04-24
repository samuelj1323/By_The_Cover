import React from "react";
import Card from "./Card";
class Carousel extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            
        }
    };
    makeItems = (movies) =>{
        return movies.map((movie) =>{

            return(
                <Card 
                    id={movie.id}
                    title={movie.title}
                    genre={movie.genre}
                    year={movie.year}
                    image={"https://image.tmdb.org/t/p/original/"}
                />
            )
        })
    }
    render(){
        return(
            <div className="rows">
                <div className="rows" style={{display:'flex', flexDirection:'row', scrollBehavior:'auto', overflowX:'scroll', }} >
                    {this.makeItems(this.props.movies)}
                </div>
            </div>
        );
    }
}
export default Carousel;