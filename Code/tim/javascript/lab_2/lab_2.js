$( document ).ready(() => {
    $('.add-item').click(() => {           
        var list_item_name = $('.input-prompt').val()
        $('.master-list').append(`<div class="list-item"><p class="todo-action">${list_item_name}</p><button  class="complete-button">Completed!</button><button class="delete-button">Deleted!</button></div>`);
        $('.complete-button').unbind('click')
        $('.complete-button').click((e) => console.log($(e.target)))
        $('.complete-button').click((e) => $(e.target).parent().find('.todo-action').toggleClass("strikethrough"))
        $('.delete-button').click((e) => $(e.target).parent().remove())
        // $('.delete-button').first().parent().remove()
        // $('.complete-button').click(() => $(this).parent().find('.todo-action').toggleClass("strikethrough"))
    });
});