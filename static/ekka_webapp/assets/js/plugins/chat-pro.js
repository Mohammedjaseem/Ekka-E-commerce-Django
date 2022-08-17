
$(document).ready(function(){

    'use strict';

    //click event on a tag for Whatsapp
    $('#cp-whatsapp').on("click",function(){
     
      var number =  $(this).attr("data-number");
      var message =  $(this).attr("data-message");
      
      //checking for device type
      if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
          // redirect link for mobile WhatsApp chat awc
          window.open('https://wa.me/'+number+'/?text='+message, '-blank');  
      }
      else{
          // redirect link for WhatsApp chat in website
          window.open('https://web.WhatsApp.com/send?phone='+number+'&text='+message, '-blank'); 
      }
    })

    // chat widget open/close duration
    $('ec-cp-style').launchBtn( { openDuration: 400, closeDuration: 300 } );
});

// chat panel open/close function
(function($) {
  
    'use strict';

    $.fn.launchBtn = function(options) {

        var mainBtn, panel, clicks, settings, launchPanelAnim, closePanelAnim, openPanel, boxClick;

        mainBtn = $(".cp-button");
        panel = $(".cp-panel");
        clicks = 0;

        //default settings
        settings = $.extend({
          openDuration: 600,
          closeDuration: 200,
          rotate: true
        }, options);

        //Open panel animation
        launchPanelAnim = function() {
          panel.animate({
            opacity: "toggle",
            height: "toggle"
          }, settings.openDuration);
        };

        //Close panel animation
        closePanelAnim = function() {
            panel.animate({
              opacity: "hide",
              height: "hide"
            }, settings.closeDuration);
        };

        //Open panel and rotate icon
        openPanel = function(e) {
          if (clicks === 0) {
              if (settings.rotate) {
                  $(this).removeClass('rotateBackward').toggleClass('rotateForward');

                  $(".cp-list").addClass('animated zoomIn');     
              }

              launchPanelAnim();
              clicks++;
          } 
          else {
              if (settings.rotate) {
                  $(this).removeClass('rotateForward').toggleClass('rotateBackward');

                  $(".cp-list").removeClass('animated zoomIn');
              }

            closePanelAnim();
            clicks--;
          }

          e.preventDefault();
          return false;
      };

      //Allow clicking in panel
      boxClick = function(e) {
        e.stopPropagation();
      };

      //Main button click
      mainBtn.on('click', openPanel);

      //Prevent closing panel when clicking inside
      panel.on('click', boxClick);

      //Click away closes panel when clicked in document
      $(document).on('click', function() {

    			closePanelAnim();

    			if (clicks === 1) {
    				mainBtn.removeClass('rotateForward').toggleClass('rotateBackward');
    			}
    			clicks = 0;
      });
    };
}(jQuery));