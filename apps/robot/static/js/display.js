$("#query").submit(function (event) {
      event.preventDefault();
      var query = $("#question").val();
      alert(query);
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/res",
        data: query,
        success: function (data) {
          alert(data);
        }
      });
});