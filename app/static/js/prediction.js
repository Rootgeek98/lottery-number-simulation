function changeBall(s, n) {
  if (n > 9) {
    $(s).attr("src", "/static/img/ball" + n + ".png");
  } else if (n === 9) {
    $(s).attr("src", "/static/img/ballNine.png");
  } else if (n === 8) {
    $(s).attr("src", "/static/img/ballEight.png");
  } else if (n === 7) {
    $(s).attr("src", "/static/img/ballSeven.png");
  } else if (n === 6) {
    $(s).attr("src", "/static/img/ballSix.png");
  } else if (n === 5) {
    $(s).attr("src", "/static/img/ballFive.png");
  } else if (n === 4) {
    $(s).attr("src", "/static/img/ballFour.png");
  } else if (n === 3) {
    $(s).attr("src", "/static/img/ballThree.png");
  } else if (n === 2) {
    $(s).attr("src", "/static/img/ballTwo.png");
  } else if (n === 1) {
    $(s).attr("src", "/static/img/ballOne.png");
  }

}

function predictByRandom() {
  $.post('/random/', "", function (data) {
    var arr = JSON.parse(data);
    changeBall("#ballOneRandom", arr[0]);
    changeBall("#ballTwoRandom", arr[1]);
    changeBall("#ballThreeRandom", arr[2]);
    changeBall("#ballFourRandom", arr[3]);
    changeBall("#ballFiveRandom", arr[4]);
    changeBall("#ballSixRandom", arr[5]);
  });
}

function predictByHighFreq() {
  var duration = $("#highFreqOption").val();
  $.post('/high-freq/', $.param({"duration": duration}), function (data) {
    var arr = JSON.parse(data);
    changeBall("#ballOneHighFreq", arr[0]);
    changeBall("#ballTwoHighFreq", arr[1]);
    changeBall("#ballThreeHighFreq", arr[2]);
    changeBall("#ballFourHighFreq", arr[3]);
    changeBall("#ballFiveHighFreq", arr[4]);
    changeBall("#ballSixHighFreq", arr[5]);
  });
}

function predictByLowFreq() {
  var duration = $("#lowFreqOption").val();
  $.post('/low-freq/', $.param({"duration": duration}), function (data) {
    var arr = JSON.parse(data);
    changeBall("#ballOneLowFreq", arr[0]);
    changeBall("#ballTwoLowFreq", arr[1]);
    changeBall("#ballThreeLowFreq", arr[2]);
    changeBall("#ballFourLowFreq", arr[3]);
    changeBall("#ballFiveLowFreq", arr[4]);
    changeBall("#ballSixLowFreq", arr[5]);
  });
}


$( document ).ready(function() {
  adjustHeight(".panel");

  $("#linkHome").show();
  
  $('#btnRandom').click(function () {
    $('#formRandom').show();
    $('#formHighFreq').hide();
    $('#formLowFreq').hide();
    predictByRandom();
  });
  
  $('#btnHighFreq').click(function () {
    $('#formRandom').hide();
    $('#formHighFreq').show();
    $('#formLowFreq').hide();
    predictByHighFreq();
  });
  
  $('#btnLowFreq').click(function () {
    $('#formRandom').hide();
    $('#formHighFreq').hide();
    $('#formLowFreq').show();
    predictByLowFreq();
  });
  
  $('#highFreqOption').change(function () {
    predictByHighFreq();
  });
  
  $('#lowFreqOption').change(function () {
    predictByLowFreq();
  });
});
