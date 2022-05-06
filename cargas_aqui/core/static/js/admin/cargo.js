(function ($) {
  $(function() {
    $('#id_driverPhone').mask('(99) 99999-999?9');

    if(!!$("#changelist").length) {
    
      var timeout;

      function scheduleReload() {
        timeout = setTimeout(function() {
          location.reload();
        }, 60 * 1000);
      }

      scheduleReload();

      $(window).on('click', function() {
        clearTimeout(timeout);
        scheduleReload();
      });
    
    }
  });

})(django.jQuery);