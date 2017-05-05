function adjustHeight(s) {
  var heights = $(s).map(function() {
      return $(this).height();
  }).get(),

  maxHeight = Math.max.apply(null, heights);

  $(s).height(maxHeight);
}
