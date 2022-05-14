const options= document.getElementById('dropDown')
let value= options.value
options.addEventListener('change', function(){
    // console.log(options.value)
     value= options.value
})
// const value= options.options[options.selectedIndex].value


// ---------------------------------------------
let secret= []
let info = []
let newMessage= []
let decryptedMessage=[]

const app = new Vue({
    el: '#app',
    data: {
        message: '',
        secret: [],
        newMessage: '',
        decrypt: '',
        decryptedMessage: '',
    },
    methods: {
        // Encrypt the message
        encryptMessage: function(message){ 

            // 
            console.log(value,'testing value')
            // console .log(message, 'message')
            // 

            for(i of message){
                let x= value
                
                // console.log(one[i])
                let num= one[i]
                x= parseInt(x)
                // 
                console.log(x.type,num, 'testing x and num value')
                console.log(typeof x, 'type of x')
                console.log(typeof num, 'type of num')
                // 
                num =((num+x) % 26)
                // 
                console.log(num,"num value")
                // 
                secret+= two[num]
            }
            this.secret= this.secret.concat({
                text:this.message, 
            })
            // secret= secret.pop()
            this.message= ""
            this.newMessage=secret
            
            secret= []
        },
        // ---------------------
        // Decrypt the message
        decryptMessage: function(message){
            // console.log(message)
            let x= value
            x= parseInt(x)
            // 
            console.log(x)
            // 
            for(i of message){
                let num= one[i]
                num =((num+x) % 26)
                // if(num = num.Math.sign(-1)){
                //     num *= -1
                // }
                // 
                console.log(num, 'num value')
                // 
                secret+= two[num]
            }
            this.decrypt= ""
            this.decryptedMessage=secret
            secret=[]
        },
        // val: function(){
        //     // console.log(options.value)
        //     value = options.value
        //     console.log(value)
        
        // },
        range: function(size, startAt =0) {
            return [...Array(size).keys()].map(i => i + startAt);
        }
    },
    created: function() {
    }
})


const one= {

    'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6,
    'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,
    'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 
    's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,
    'y' :25, 'z' : 26,
}
const two= {
    0 : 'z', 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f',
    7 : 'g', 8: 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 
    14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't',
    21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 
}
// '''
// Lab 7 V.2

// '''

// def rot_cipher_encrypt(message:str,shift:int):
//     encrypt_dict = {  
//     'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6,
//     'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,
//     'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 
//     's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,
//     'y' :25, 'z' : 26, 
// }
//     decrypt_dict = {  
//     0 : 'z', 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f',
//     7 : 'g', 8: 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 
//     14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't',
//     21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 
// }
//     encrypted_text = ''
//     for letter in message:
//         num = encrypt_dict[letter]
//         num = ((num + shift) % 26)
//         encrypted_text += decrypt_dict[num]
//     return encrypted_text
   

// def rot_cipher_decrypt(message:str,shift:int):
//     encrypt_dict = {  
//     'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6,
//     'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,
//     'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 
//     's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,
//     'y' :25, 'z' : 26, 
// }
//     decrypt_dict = { 
//     0 : 'z', 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f',
//     7 : 'g', 8: 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 
//     14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't',
//     21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 
// } 
//     decrypt_text = ''
//     for letter in message:
//         num = encrypt_dict[letter]
//         num = ((num - shift) % 26)
//         decrypt_text += decrypt_dict[num]
//     return decrypt_text

// message = 'longstringofwords'
// shift = 19
// encrypted_message = rot_cipher_encrypt(message, shift)
// print(encrypted_message) # xubbe
// decypted_message = rot_cipher_decrypt(encrypted_message, shift)
// print(decypted_message) # hello


