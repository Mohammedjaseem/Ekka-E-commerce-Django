/**
    Item Name: Ekka - Ecommerce HTML Template.
    Author: ashishmaraviya
    Copyright 2021-2022
	Author URI: https://themeforest.net/user/ashishmaraviya
**/
(function($) {
    "use strict";

    /*--------------------- Main Slider image auto height ---------------------- */
    
    $(document).ready(function() {

        // Comment this Two below line to display Popup evertime
        var dataValue = false; 
        ecCreateCookie('ecPopNewsLetter',dataValue,1);

        var ecPopNewsLetter = ecAccessCookie("ecPopNewsLetter");
        if (ecPopNewsLetter == "false")
        {
            setTimeout( function(){ 
                $("#ec-popnews-bg").fadeIn();
                $("#ec-popnews-box").fadeIn();
            }, 5000);

            $("#ec-popnews-close").click(() => {
                $("#ec-popnews-bg").fadeOut();
                $("#ec-popnews-box").fadeOut();

                var dataValue = true;
                ecCreateCookie('ecPopNewsLetter',dataValue,1);
            });

            $("#ec-popnews-bg").click(() => {
                $("#ec-popnews-bg").fadeOut();
                $("#ec-popnews-box").fadeOut();

                var dataValue = true;
                ecCreateCookie('ecPopNewsLetter',dataValue,1);
            });
        }
    });

})(jQuery);




