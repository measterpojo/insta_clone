
console.log('was cookin')

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})





$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})



// window.onload = function()
// {
//     if (window.jQuery)
//     {
//         alert('jQuery is loaded');
//     }
//     else
//     {
//         alert('jQuery is not loaded');
//     }
// }