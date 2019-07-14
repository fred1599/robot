function test(){
    var value = document.getElementById('question').value;
    if (value){
        $.ajax({
            url: "{{ url_for('/result') }}",
            type: 'post',
            datatype: "text",
            data: ({'question': value}),
            success: function(data){
                alert(data);
                return data;
            },
            error: function() {
                alert('Error occured');
            }
        });
    }
}