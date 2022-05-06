(function ($) {
  $(function() {
    $('#id_driverPhone').mask('(99) 99999-999?9');

    if(!!$("#changelist").length) {
    
      var timeout;

      function scheduleReload() {
        console.log("agendando");
        timeout = setTimeout(function() {
          console.log("reloadando");
          location.reload();
        }, 60 * 1000);
      }

      scheduleReload();

      $(window).on('click', function() {
        console.log("limpando");
        clearTimeout(timeout);
        scheduleReload();
      });
    
    }
  });

})(django.jQuery);