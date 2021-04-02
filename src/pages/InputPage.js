import React from 'react';
class InputPage extends React.Component{
    constructor(props){
        super(props);
        this.state={

        }
        
    }
    render(){
        return(
            <div className="opening-page" style={{ alignItems:'center',justifyItems:'center', flex:1, flexDirection:'row'}}> {/** This is the background */}
          
                <div className="input-box">
                    <h1>By The Cover</h1>
                    <h3>Enter a comma dillineated list of movies that you would be in the mood to watch tonight!</h3>
                    <label style={{fontSize:32}}>
                        Movies: 
                        <input style={{width: 400, height:25}} type="text" name="movies"/>
                    </label>
                    <div style={{marginTop:30}}>
                        <input style={{height:35, fontSize:20, borderRadius:5, backgroundColor:'purple'}} type="submit" name="submit"/>
                    </div>
                
                </div>
          
            </div>   
        );
    }
}
export default InputPage;