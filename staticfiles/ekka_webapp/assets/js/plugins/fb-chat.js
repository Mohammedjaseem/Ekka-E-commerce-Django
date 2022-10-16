$(document).ready(function(){
    
    // chat widget open/close duration
    $('ec-fb-style').launchBtn( { openDuration: 400, closeDuration: 300 } );
});

// chat panel open/close function
(function($) {
  
    'use strict';

    $.fn.launchBtn = function(options) {

        var mainBtn, panel, clicks, settings, launchPanelAnim, closePanelAnim, openPanel, boxClick;

        mainBtn = $(".fb-button");
        panel = $(".fb-panel");
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
            }

            launchPanelAnim();
            clicks++;
          } 
          else {
              if (settings.rotate) {
                $(this).removeClass('rotateForward').toggleClass('rotateBackward');
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
      panel.click(boxClick);

      //Click away closes panel when clicked in document
      $(document).click(function() {
			closePanelAnim();
			if (clicks === 1) {
				mainBtn.removeClass('rotateForward').toggleClass('rotateBackward');
			}
			clicks = 0;
      });
    };
}(jQuery));