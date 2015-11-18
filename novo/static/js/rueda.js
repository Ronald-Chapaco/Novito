$(function () {

  $("#comment").focus(function () {
    $(this).attr("rows", "3");
    $("#comment-helper").fadeIn();
  });

  $("#comment").blur(function () {
    $(this).attr("rows", "1");
    $("#comment-helper").fadeOut();
  });

  $("#comment").keydown(function (f) {
    var keyCode = f.which?f.which:f.keyCode;
    if (f.ctrlKey && (keyCode == 10 || keyCode == 13)) {
      $.ajax({
        url: "/social/commentrue/",
        data: $("#comment-form").serialize(),
        cache: false,
        type: 'post',
        success: function (data) {
          $("#comment-list").html(data);
          var comment_count = $("#comment-list .comment").length;
          $(".comment-count").text(comment_count);
          $("#comment").val("");
          $("#comment").blur();
        }
      });
    }
  });


});