$( document ).ready(() => {
    $('.submit-button').click(() => {            
        var chance = Chance();
        var pass_length = $('.input-prompt').val();
        // console.log(pass_length);
        var password = "";
        for (var a = 0;a<pass_length ;a++ ) {
            password += chance.character();
        } 
        $('.output').text("Your password is " + password)
    });
// alert("Your password is " + password);
});