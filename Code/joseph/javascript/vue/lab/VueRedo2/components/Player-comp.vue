<template>
<!-- Images for Rock, Paper Scissors -->
<div class="container">
    <img type="button" class="img" src="../assets/rock.jpg" v-on:click="rockPicked()" />
    <img type="button" class="img" src="../assets/paper.jpg" v-on:click="paperPicked()" />
    <img type="button" class="img" src="../assets/scissors.jpg" v-on:click="scissorsPicked()" />
</div>
</template>

<script>
export default {
    // Methods
    methods: {
        rockPicked() {
            this.$emit('getPick', 'rock')
        },
        paperPicked() {
            this.$emit('getPick', 'paper')
        },
        scissorsPicked() {
            this.$emit('getPick', 'scissors')
        },
    }
};
</script>
<!-- css scoped styling -->
<style scoped>

.container {
    display: grid;    
}

.img {
    cursor:pointer;
    margin: 15px;
    height: 125px;
    width: 87px;
    transform: rotate(90deg);
    border-radius: 10px;
}
</style>