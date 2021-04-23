import React from 'react';
//import Link from 'react';
import {BrowserRouter as Router, Switch, Route, useHistory,Redirect, Link} from 'react-router-dom'
import RecPage from './RecPage'
import Button from 'react-bootstrap/Button'
import 'bootstrap/dist/css/bootstrap.min.css';
import { FormControl, InputGroup, Spinner } from 'react-bootstrap';
class InputPage extends React.Component{
    constructor(props){
        super(props);
        this.state={
            show_rec:false,
            movies: "",
            rec_movies:[
                {
                    title:'Star Wars',
                    genre:'',
                    year: '2002',
                    image: null
                },
                {
                  title:'Guardians of the Galaxy',
                  genre:'',
                  year: '',
                  image: null
                },
                {
                  title:'Wonder Years',
                  genre:'',
                  year: '2002',
                  image: null
                },
                {
                  title:'Finding Nemo',
                  genre:'',
                  year: '2002',
                  image: null
                },
                {
                  title:'Big Hero 6',
                  genre:'',
                  year: '2002',
                  image: null
                },
                {
                title:'Iron Man',
                genre:'',
                year: '2002',
                image: null
                },
                {
                title:'Captain America',
                genre:'',
                year: '2002',
                image: null
                },
                {
                title:'Superman',
                genre:'',
                year: '2002',
                image: null
                },
                {
                title:'Batman',
                genre:'',
                year: '2002',
                image: null
                },
                {
                title:'Titanic',
                genre:'',
                year: '2002',
                image: null
                },
            ]
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleClick = this.handleClick.bind(this)
        
    }
    handleClick(){ // here is where we will call the API
        //alert("movies we are searching: " + this.state.movies)
        this.setState({show_rec:'loading'})
        setTimeout(function(){
            this.setState({show_rec:'show'})}.bind(this)
        , 10000)
    }
    handleChange(event){ // Here is where the value is being passed in so the API can use it
        this.setState({movies: event.target.value})
    }
    
    
    
    
    render(){

        const renderAuthButton = () =>{
            if(this.state.show_rec === "show"){
                return <RecPage movies={this.state.rec_movies}/>
            }else if(this.state.show_rec === "loading"){
                return (
                <div style={{height:'100vh', textAlign:'center',color:'slategray'}}>
                    <h1>Thank you for your patience, we are loading your movies</h1>
                    <div>
                    <Spinner variant="light" style={{position:'absolute', left:'30%',top:'25%',width:800, height:800}} animation="border" role="status" size="lg">
                        <span className="sr-only"> Loading...</span>
                    </Spinner>

                    </div>
                    
                </div>
                );
            }else{
                return (
                <div style={{height:'100vh',textAlign:'center',color:'slategray'}}>
                    <h1>Please Enter your movies above in a comma dilleanted list.</h1>
                </div>
                );
                
            }
        }
        return(
            <div  style={{display:'flex', flexDirection:'column', backgroundColor:'black',flex:1}}>
                <div style={{height:80, backgroundColor:'black',display:'flex', flexDirection:'row'}}>
                  <h1 style={{color:'white', fontSize:35, width:250}}>By The Cover</h1>
                  
                    <InputGroup className="mb-3">
                        <InputGroup.Prepend >
                            <InputGroup.Text id="basic-addon1" >Movies</InputGroup.Text>
                            </InputGroup.Prepend>
                            <FormControl style={{ height:70, width:800}}
                                placeholder="What's an example of a movie you'd like to watch?"
                                aria-label="Username"
                                aria-describedby="basic-addon1"
                                value={this.state.movies}
                                onChange={this.handleChange}
                            />
                        </InputGroup>
                    <Button variant="dark" style={{height:70}} onClick={this.handleClick}>Search</Button>
                </div>
                {renderAuthButton()}
                

            </div>
              
        );
    }
}
export default InputPage;