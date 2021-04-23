import { render } from "@testing-library/react";
import React from "react";

function Card(props){
   // const card_img = fetch("https://api.themoviedb.org/3/movie/"+this.props.id+"?api_key=KEY_here&language=en-US")["poster_path"]
    return(
        <div 
         style={
             {  minWidth:250,
                minHeight:420,  
                backgroundColor:"black",
                color:'white',
                border:10,
                borderRadius:10,
                margin:10,
                textAlign:'center'}
            }
        >
            <div>
                <img src={"https://image.tmdb.org/t/p/original/"} width={250} height={420}/>
            </div>
            <a>{props.title+",\n"}</a>
            <a>{props.genre}</a>
            
            
        </div>
    );
        
}
export default Card;
