//import { render } from "@testing-library/react";
import React from "react";
//import {img} from 'react';
function Card(props){
   
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
                textAlign:'center',
            }
            }
        >
            <div>
                <img src={props.image} width={250} height={420}/>
            </div>
            <a>{props.title+"\n"}</a>
            
            
            
        </div>
    );
        
}
export default Card;