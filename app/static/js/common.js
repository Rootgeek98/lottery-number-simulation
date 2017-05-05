function adjustHeight(cls) {
  var heights = $(cls).map(function() {
      return $(this).height();
  }).get(),

  maxHeight = Math.max.apply(null, heights);

  $(cls).height(maxHeight);
}
