$(document).ready(function() {
     $('form').on('submit', function(event) {
       $.ajax({
          data : {
             question : $('#question').val(),
                 },
             type : 'POST',
             url : '/question',
       })
     });
});
