$("#query").submit(function () {
      var query = $("#question").val();
      $.ajax({
        type: "POST",
        url: $SCRIPT_ROOT + "/result",
        data: query,
        dataType: 'text',
        success: function (data) {
          alert(data);
        }
      });
});