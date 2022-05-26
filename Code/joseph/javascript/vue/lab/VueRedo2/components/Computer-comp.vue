<template>
<div class="container">
    <img type="button" class="img" src="../assets/play-game.png" v-on:click="computerPick()">
    <div class="middle">
        <div class="text">RPS?</div>
    </div>
</div>
</template>

<script>
const picks = ["rock", "paper", "scissors"];
export default {
    data() {
        return {
            pick: ""            
        };
    },

    methods: {
        computerPick() {
            const computerPickIndex = Math.floor(Math.random() * picks.length);
            this.pick = picks[computerPickIndex];
            this.$emit('getPick', this.pick);
        },
    }
};
</script>
<!-- css scoped styling -->
<style scoped>
.img {    
    margin: 0 auto;
    margin-bottom: 7px;
    padding: 16px 32px;    
    display: inline-block;
    height: 128px;
    width: 128px;
    border-radius: 7px;
    cursor: pointer;
    opacity:1;
    transition: .5s ease;
    backface-visibility: hidden;
}

.middle {
    transition: .5s ease;
    opacity: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    text-align: center;
}

.container:hover .img {
    opacity: 0.3;
}

.container:hover .middle {
    opacity: 1;
}

.text {
    background-color: #04AA6D;
    color: white;
    font-size: 16px;
    padding: 16px 32px;    
}

</style>