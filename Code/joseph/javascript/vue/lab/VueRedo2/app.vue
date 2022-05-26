<template>
<div id="app">
    <div class="header-container">
        <h1>Welcome to Rock, Paper, Scissors!!!</h1>
    </div>
    <div class="howtoplay">
        <h3>Click your pick, then press the controller icon!</h3>
    </div>
    <div class="float-player">
        <Player v-on:getPick="updatePlayerPick($event)" v-bind:pick="player_pick" />
        <h2 style="color:antiquewhite">You Picked: {{player_pick}}</h2>
    </div>
    <div class="float-computer">
        <Computer @click="play" v-on:getPick="updateComputerPick($event)" v-bind:pick="computer_pick" />
        <img type="button" v-if="!computer_pick" src="./assets/qmark.jpg" />
        <img class="computer_img" type="button" v-if="!!computer_pick" :src="require('./assets/'+ImgSrc())" />
        <h2 style="color:azure">The Computer Picked: {{computer_pick}}</h2>
    </div>
    <h1 class="winner" v-if="winner">
    {{ winner }}
    </h1>
</div>
</template>

<script>
import Player-comp from './components/Player-comp.vue'
import Computer-comp from './components/Computer-comp.vue'

const picks = ["rock", "paper", "scissors"];
export default {
    name: 'RPS',
    components: {
        Player,
        Computer,
    },
    data() {
        return {
            player_pick: "",
            computer_pick: "",
            winner: ""
        };        
    },
    methods: {
        updatePlayerPick(pick) {
            this.player_pick = pick;            
        },
        updateComputerPick(pick) {
            this.computer_pick = pick;            
        },
        ImgSrc() {
            if (this.computer_pick == "rock") {
                return "rock.jpg"
            }
            else if (this.computer_pick == "paper") {
                return "paper.jpg"
            }
            else {
                return "scissors.jpg"
            }
        },
        play() {
            const {player_pick, computer_pick} = this;
            if (player_pick == computer_pick) {
                this.winner = "It's a tie!";
            } else if (
                (player_pick === "paper" && computer_pick === "scissors") ||
                (player_pick === "rock" && computer_pick === "paper") ||
                (player_pick === "scissors" && computer_pick === "rock")
            ) {
                this.winner = "Computer Won";
            } else if (player_pick === "") {
                alert("You have to pick!!")                
            }
            else {
                this.winner = "You Won!";
            }
        }
    }
}
</script>

<style>
*, .body {
    background-color: #1f2127;
    overflow: hidden;
}

* {
    margin: 0;
    padding: 0;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    font-family: "Comic Sans MS", cursive, sans-serif, 'Times New Roman', Times, serif;
    font-weight: 657;
}

.howtoplay {
    padding: 10px;
    margin-left: 200px;
    width: 70%;
}

.howtoplay h3 {
    text-align: center;
    border: 2px solid goldenrod;
}

.header-container {
    background: bisque;
    padding: 20px;
    text-align: center;
}

.header-container h1 {
    background-color: bisque;
    color: #1f2127;
    text-align: center;
    font-family: "Comic Sans MS", cursive, sans-serif, 'Times New Roman', Times, serif;
}

.float-player {
    background-color:gainsboro;
    width: 50%;
    float: left;
    padding: 20px;
}

.float-computer {
    background-color:gainsboro;
    width: 50%;
    float: left;
    padding: 20px;
    margin-left: 200px;
}

.computer_img {
    transform: rotate(-90deg);
    height: 125px;
    width: 87px;
    padding-left: 20px;
    border-radius: 10px;
}

.winner {
    width: 320px;
    padding: 10px;
    border: 5px solid #303030;
    margin: 0;
    background-color: #ff7d4e;
    color: bisque;
}

</style>