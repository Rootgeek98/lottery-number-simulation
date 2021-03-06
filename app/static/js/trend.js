function callHistogram() {
  var duration = $("#histOption").val();

  $.get("/histogram/", "duration=" + duration, function(data) {
    $("#histogram").attr("src", "/histogram/?duration=" + duration);
  });
}

function callEvent() {
  var duration = $("#eventOption").val();

  $.get("/event/", "duration=" + duration, function(data) {
    $("#event").attr("src", "/event/?duration=" + duration);
  });
}

function showHistogram() {
  $("#histForm").show();
  $("#eventForm").hide();
}

function showEvent() {
  $("#histForm").hide();
  $("#eventForm").show();
}

$(document).ready(function() {
  adjustHeight(".panel");

  $("#linkHome").show();

  callHistogram();
  $("#histOption").change(function() {
    callHistogram();
  });

  callEvent();
  $("#eventOption").change(function() {
    callEvent();
  });

  $("#histButton").click(function() {
    showHistogram();
  });

  $("#eventButton").click(function() {
    showEvent();
  });
});
