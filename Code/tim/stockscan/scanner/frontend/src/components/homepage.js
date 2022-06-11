import React, { Component } from "react";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
        this.state= {symbol:"AAPL"} ;
        this.load();
        
    }
    async load() {
        var response = await fetch(`/api/get_user_history`)
        var user_history_json = await response.json(); 
        console.log(user_history_json)
        this.setState({
            user_history_json:user_history_json
        })
    }
    
    render() {

        return (<div>
            <span ClassName='text'>Enter a symbol</span>
            <input className="input-prompt" type="text" onChange={(input)=>this.setState({symbol:input.target.value})}/>
            <button className="add symbol" onClick={async ()=>{
                console.log(this.state.symbol)
                var response = await fetch(`https://api.twelvedata.com/rsi?symbol=${this.state.symbol}&interval=30min&apikey=ea9700758b324887a09d259878f264a2`) 
                const Master_list = await response.json();

                var search = await fetch(`/api/save_history?search=${this.state.symbol}`)
                
                this.setState({result:Master_list.values[0].rsi});
            }} type="submit">Lookup Symbol</button>
            <p>{this.state.result?`The most recent RSI value for ${this.state.symbol} is ${this.state.result}.`:""}</p>
            
            {this.state.user_history_json && this.state.user_history_json.historical_searches.split(',').map(p=>{
                console.log(p)
                return (<p>{p}</p>)
            })}
        </div>
        )
    }
}