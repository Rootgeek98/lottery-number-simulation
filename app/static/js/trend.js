function callHistogram() {
  var duration = $("#histOption").val();

  $("#histogram").attr("src", "/histogram/?duration=" + duration);
}

function callEvent() {
  var duration = $("#eventOption").val();

  $("#event").attr("src", "/event/?duration=" + duration);
}

function showHistogram() {
  $("#histForm").show();
  $("#eventForm").hide();
}

function showEvent() {
  $("#histForm").hide();
  $("#eventForm").show();
}

$( document ).ready(function() {
    var heights = $(".panel").map(function() {
        return $(this).height();
    }).get(),

    maxHeight = Math.max.apply(null, heights);

    $(".panel").height(maxHeight);

    $("#linkHome").show();

    callHistogram();
    $("#histOption").select(function () {
      callHistogram();
    });

    callEvent();
    $("#eventOption").select(function () {
      callEvent();
    });

    $("#histButton").click(function () {
      showHistogram();
    });

    $("#eventButton").click(function () {
      showEvent();
    });
});
