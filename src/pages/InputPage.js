import React from 'react';
//import Link from 'react';
//import {BrowserRouter as Router, Switch, Route, useHistory,Redirect, Link} from 'react-router-dom'
import RecPage from './RecPage'
import Button from 'react-bootstrap/Button'
import 'bootstrap/dist/css/bootstrap.min.css';
import { FormControl, InputGroup, Spinner } from 'react-bootstrap';
//import { findAllInRenderedTree } from 'react-dom/test-utils';
class InputPage extends React.Component{
    constructor(props){
        super(props);
        this.state={
            show_rec:false,
            movies: "",
            rec_movies1:
            [
                {
                    title:'Nothing was returned',
                    image: 'https://image.tmdb.org/t/p/original//6EiRUJpuoeQPghrs3YNktfnqOVh.jpg'
                }
            ],
            rec_movies2:
            [
                {
                    title:'Nothing was returned',
                    image: 'https://image.tmdb.org/t/p/original//78lPtwv72eTNqFW9COBYI0dWDJa.jpg'

                }
            ],
            rec_movies3:
            [
                {
                    title:'Nothing was returned',
                    image: 'https://image.tmdb.org/t/p/original//78lPtwv72eTNqFW9COBYI0dWDJa.jpg'

                }
            ],
            rec_movies4:
            [
                {
                    title:'Nothing was returned',
                    image: 'https://image.tmdb.org/t/p/original//78lPtwv72eTNqFW9COBYI0dWDJa.jpg'

                }
            ],
            rec_movies5:
            [
                {
                    title:'Nothing was returned',
                    image: 'https://image.tmdb.org/t/p/original//78lPtwv72eTNqFW9COBYI0dWDJa.jpg'

                }
            ],
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleClick = this.handleClick.bind(this)
        
    }
    handleClick(){ // here is where we will call the API
        //alert("movies we are searching: " + this.state.movies)
        this.setState({show_rec:'loading'})
        //{
        //    "title": "asjd;flajs",
        //    "image": "als"
        //}
        let movies_passed = this.state.movies
        let pushed_movies = ""
        for(let i = 0; i < movies_passed.length; i++ ){
 //           if(movies_passed[i] === " "){
 //               pushed_movies += "_"
 //           }else{
                pushed_movies += movies_passed[i] 
 //           }
        }
        let url_passed = "/search_movie/"+pushed_movies
        fetch(url_passed).then(res => res.json()).then(data =>{
            var new_data1 = data.top_10_posters;
            var new_data2 = data.bottom_10_posters;
            var new_data3 = data.top_10_soundtracks;
            var new_data4 = data.bottom_10_soundtracks;
            var new_data5 = data.sound_then_poster;
            let i = 0;
            let arr1 = [];
            let arr2 = [];
            let arr3 = [];
            let arr4 = [];
            let arr5 = []
            for(i = 0; i < new_data1.length; i++){
                var obj1 = JSON.parse(new_data1[i]);
                var obj2 = JSON.parse(new_data2[i]);
                var obj3 = JSON.parse(new_data3[i]);
                var obj4 = JSON.parse(new_data4[i]);
                var obj5 = JSON.parse(new_data5[i]);
                arr1.push(obj1)
                arr2.push(obj2)
                arr3.push(obj3)
                arr4.push(obj4)
                arr5.push(obj5)
                //alert(obj)
            }
            this.setState({rec_movies1:arr1})
            this.setState({rec_movies2:arr2})
            this.setState({rec_movies3:arr3})
            this.setState({rec_movies4:arr4})
            this.setState({rec_movies5:arr5})
            
        })
        setTimeout(function(){
            this.setState({show_rec:'show'})}.bind(this)
        , 5000)
    }
    handleChange(event){ // Here is where the value is being passed in so the API can use it
        this.setState({movies: event.target.value})
    }

    
    
    
    
    render(){

        const renderAuthButton = () =>{
            if(this.state.show_rec === "show"){
                return <RecPage movies1={this.state.rec_movies1} movies2={this.state.rec_movies2} movies3 ={this.state.rec_movies3} movies4={this.state.rec_movies4} movies5={this.state.rec_movies5}/>
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