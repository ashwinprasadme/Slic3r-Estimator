$(function() {

  $('#quality').switchy();
  $('#speed').switchy();
  $('#support').switchy();

  $('#quality').on('change', function(){

    // Animate Switchy Bar background color
    var bgColor = '#FF8700';

    if ($(this).val() == '100'){
      bgColor = '#24BC21';
    } else if ($(this).val() == '200'){
      bgColor = '#7fcbea';
    }
      else if ($(this).val() == '300'){
      bgColor = '#ED4A4A';
    }

    // Display action in console
    var log =  'Resolution  " '+$(this).val()+' "'+' mm';
    $('#console').html(log).hide().fadeIn();
  });


  $('#speed').on('change', function(){

    // Animate Switchy Bar background color
    var bgColor = '#FF8700';

    if ($(this).val() == '60'){
      bgColor = '#24BC21';
    } else if ($(this).val() == '70'){
      bgColor = '#7fcbea';
    }
      else if ($(this).val() == '80'){
      bgColor = '#ED4A4A';
    }



    // Display action in console
    var log =  'Speed  " '+$(this).val()+' "'+' mm/s';
    $('#console2').html(log).hide().fadeIn();
  });

    $('#support').on('change', function(){

      var log =  'Support: " '+$(this).val()+' "';
      $('#console3').html(log).hide().fadeIn();
    });

});
