/**
    Item Name: Ecart - Multi Vendor Ecommerce HTML Template.
    Author: ashishmaraviya
    Version: 3.2
    Copyright 2021
	Author URI: https://themeforest.net/user/ashishmaraviya
**/
// Function To Create New Cookie 
function ecCreateCookie(cookieName,cookieValue,daysToExpire)
{
    var date = new Date();
    date.setTime(date.getTime()+(daysToExpire*24*60*60*1000));
    document.cookie = cookieName + "=" + cookieValue + "; expires=" + date.toGMTString();
}

// Function To Delete Existing Cookie
function ecDeleteCookie(cookieName,cookieValue)
{
    var date = new Date(0).toGMTString();
    document.cookie = cookieName + "=" + cookieValue + "; expires=" + date;
}

// Function To Access Existing Cookie
function ecAccessCookie(cookieName)
{
    var name = cookieName + "=";
    var allCookieArray = document.cookie.split(';');
    for(var i=0; i<allCookieArray.length; i++)
    {
        var temp = allCookieArray[i].trim();
        if (temp.indexOf(name)==0){
            return temp.substring(name.length,temp.length);
        }
    }

    return "";
}

// Function To Check Existing Cookie
function ecCheckCookie()
{
    var bgImageMode = ecAccessCookie("bgImageModeCookie");
    if (bgImageMode != "")
    {     
        var bgIDClass = bgImageMode.split('||');
        var bgID = bgIDClass[0];
        var bgClass = bgIDClass[1];
        
        $("body").removeClass("body-bg-1");
        $("body").removeClass("body-bg-2");
        $("body").removeClass("body-bg-3");
        $("body").removeClass("body-bg-4");
    
        $("body").addClass(bgClass);
    
        $("#bg-switcher-css").attr("href", "assets/demo-5/css/backgrounds/" + bgID + ".css");
    }

    var rtlMode = ecAccessCookie("rtlModeCookie");
    if (rtlMode != "")
    {
        // alert(rtlMode);    
        var $link = $('<link>', {
            rel: 'stylesheet',
            href: 'assets/demo-5/css/rtl.css',
            class: 'rtl'
        });
        $(".ec-tools-sidebar .ec-change-rtl").toggleClass('active');
        $link.appendTo('head');                
    }

    // ecCreateCookie('bgImgModeCookie',bgIDClass,1);

    var darkMode = ecAccessCookie("darkModeCookie");
    if (darkMode != "")
    {
        var $link = $('<link>', {
            rel: 'stylesheet',
            href: 'assets/demo-5/css/dark.css',
            class: 'dark'
        });
        
        $("link[href='assets/demo-5/css/responsive.css']").before($link);

        $(".ec-tools-sidebar .ec-change-mode").toggleClass('active');
        $("body").addClass("dark");
    }
    else
    {
        var themeColor = ecAccessCookie("themeColorCookie");
        if (themeColor != "")
        {
            $('li[data-color = '+themeColor+']').toggleClass('active').siblings().removeClass('active');
            $('li[data-color = '+themeColor+']').addClass('active');
            
            if(themeColor != '01'){
                $("link[href='assets/demo-5/css/responsive.css']").before('<link rel="stylesheet" href="assets/demo-5/css/skin-'+themeColor+'.css" rel="stylesheet">');
            }
        }
    }
}

(function($) {

    /*--------------------- START Site Cookie function --------------------*/
    // Calling Function On Each Time Site Load | Reload
    ecCheckCookie();

    // $(".slick-next").trigger("click");    
    $(".quickview").on("click", function(e){
        // alert();
        $(".slick-next").trigger("click");
    }); 
    

    // On click method for Clear Cookie
    $(".clear-cach").on("click", function (e) {
        ecDeleteCookie("rtlModeCookie", "");
        ecDeleteCookie("darkModeCookie", "");
        ecDeleteCookie("themeColorCookie", "");
        ecDeleteCookie("bgImageModeCookie", "");
        location.reload();
    });

    /*----------------------------- Site Loader --------------------*/
    $(window).load(function () { 
        $("#ec-overlay").fadeOut("slow"); 
    });
   
    /*----------------------------- Bootstrap dropdown   --------------------*/
    $('.dropdown').on('show.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
    });

    $('.dropdown').on('hide.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
    });

    /*----------------------------- Language and Currency Click to Active -------------------------------- */
    $(document).ready(function() {
        $(".header-top-lan li").click(function() {
            $(this).addClass('active').siblings().removeClass('active');
        });
        $(".header-top-curr li").click(function() {
            $(this).addClass('active').siblings().removeClass('active');
        });
    });

    /*----------------------------- category Toggle Bar --------------------- */
    jQuery(".ec-category-toggle").click(function(){
        jQuery(this).parent().toggleClass('active');
        jQuery("#ec-category-menu").slideToggle('slow');
    });

    jQuery(".ec-search-cat-title").click(function(){
        jQuery(this).parent().toggleClass('active');
        jQuery(".ec-search-cat-block").slideToggle('slow');
    });

    /*--------------------- Add To Whishlist -----------------------------------*/
    $("body").on("click", ".wishlist", function(){

        var count = $(".ec-wishlist-count").html();        
        count++;
        $(".ec-wishlist-count").html(count); 
        
    });

    /*--------------------- Add To Cart -----------------------------------*/
    $("body").on("click", ".add-to-cart", function(){
       
        var count = $(".ec-cart-count").html();        
        count++;
        $(".ec-cart-count").html(count);

        // Remove Empty message    
        $(".emp-cart-msg").parent().remove();        
        
        // get an image url
        var img_url = $(this).parents().parents().parents().children(".ec-pro-image-outer").find(".main-image").attr("src");
        var p_name = $(this).parents().parents().parents().find(".ec-pro-title").children().html();
        var p_price = $(this).parents().parents().parents().find(".ec-price").children(".new-price").html();
        
        var p_html = '<li>'+
                        '<a href="product.html" class="sidecart_pro_img"><img src="'+ img_url +'" alt="product"></a>'+
                        '<div class="ec-pro-content">'+
                            '<a href="product.html" class="cart_pro_title">'+ p_name +'</a>'+
                        '<span class="cart-price"><span>'+ p_price +'</span> x 1</span>'+
                            '<div class="qty-plus-minus"><div class="dec ec_qtybtn">-</div>'+
                                '<input class="qty-input" type="text" name="ec_qtybtn" value="1">'+
                            '<div class="inc ec_qtybtn">+</div></div>'+
                            '<a href="javascript:void(0)" class="remove">×</a>'+
                        '</div>'+
                    '</li>';

        $('.eccart-pro-items').append(p_html);    
        
    });

    (function() {
        var $ecartToggle = $(".ec-side-toggle"),
        $ecart = $(".ec-side-cart"),
        $ecMenuToggle = $(".mobile-menu-toggle");

        $ecartToggle.on("click", function(e) {
            e.preventDefault();
            var $this = $(this),
            $target = $this.attr("href");
            // $("body").addClass("ec-open");
            $(".ec-side-cart-overlay").fadeIn();
            $($target).addClass("ec-open");
            if ($this.parent().hasClass("mobile-menu-toggle")) {
                $this.addClass("close");
                $(".ec-side-cart-overlay").fadeOut();
            }
        });
        
        $(".ec-side-cart-overlay").on("click", function(e) {
            $(".ec-side-cart-overlay").fadeOut();
            $ecart.removeClass("ec-open");
            $ecMenuToggle.find("a").removeClass("close");
        });

        $(".ec-close").on("click", function(e) {
            e.preventDefault();
            $(".ec-side-cart-overlay").fadeOut();
            $ecart.removeClass("ec-open");
            $ecMenuToggle.find("a").removeClass("close");
        });

        $("body").on("click", ".ec-pro-content .remove", function(){

        // $(".ec-pro-content .remove").on("click", function () {
            
            var cart_product_count = $(".eccart-pro-items li").length;
            
            $(this).closest("li").remove();
            if (cart_product_count == 1) {
                $('.eccart-pro-items').html('<li><p class="emp-cart-msg">Your cart is empty!</p></li>');
            }

            var count = $(".ec-cart-count").html();            
            count--;
            $(".ec-cart-count").html(count);

            cart_product_count--;
        });    
        
    })();
   
    /*----------------------------- SideCart And  SideMenu -----------------------------------*/
    (function() {
        var $ecartToggle = $(".ec-side-toggle"),
        $ecart = $(".ec-side-cart"),
        $ecMenuToggle = $(".mobile-menu-toggle");

        $ecartToggle.on("click", function(e) {
            e.preventDefault();
            var $this = $(this),
            $target = $this.attr("href");
            // $("body").addClass("ec-open");
            $($target).addClass("ec-open");
            if ($this.parent().hasClass("mobile-menu-toggle")) {
                $this.addClass("close");
            }
        });
        $(".ec-close").on("click", function(e) {
            e.preventDefault();
            // $("body").removeClass("ec-open");
            $ecart.removeClass("ec-open");
            $ecMenuToggle.find("a").removeClass("close");
        });
    })();

    /*----------------------------- ecart Responsive Menu -----------------------------------*/
    function ResponsiveMobileEcartMenu() {
        var $ecartNav = $(".ec-menu-content, .overlay-menu"),
        $ecartNavSubMenu = $ecartNav.find(".sub-menu");
        $ecartNavSubMenu.parent().prepend('<span class="menu-toggle"></span>');

        $ecartNav.on("click", "li a, .menu-toggle", function(e) {
            var $this = $(this);
            if ($this.attr("href") === "#" || $this.hasClass("menu-toggle")) {
                e.preventDefault();
                if ($this.siblings("ul:visible").length) {
                    $this.parent("li").removeClass("active");
                    $this.siblings("ul").slideUp();
                    $this.parent("li").find("li").removeClass("active");
                    $this.parent("li").find("ul:visible").slideUp();
                } else {
                    $this.parent("li").addClass("active");
                    $this.closest("li").siblings("li").removeClass("active").find("li").removeClass("active");
                    $this.closest("li").siblings("li").find("ul:visible").slideUp();
                    $this.siblings("ul").slideDown();
                }
            }
        });
    }

    ResponsiveMobileEcartMenu();

    /*----------------------------- Main Slider ---------------------- */
    $('.ec-slider').slick({
        rows: 1,
        dots: true,
        arrows: false,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        /*vertical: true,*/
        customPaging : function(slider, i) {
            var thumb = $(slider.$slides[i]).data();
            return '0' + (i + 1);
        },
    });

    /*--------------------------- Quick view Slider ------------------------------ */
    $('.qty-product-cover').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: false,
        asNavFor: '.qty-nav-thumb',
    });

    $('.qty-nav-thumb').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.qty-product-cover',
        dots: false,
        arrows: true,
        focusOnSelect: true,
        responsive: [
        {
            breakpoint: 479,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 2,
            }
        }
        ]
    });

    /*---------------------------- Qty Plus Minus Button  ------------------------------ */
    var QtyPlusMinus = $(".qty-plus-minus");
    QtyPlusMinus.prepend('<div class="dec ec_qtybtn">-</div>');
    QtyPlusMinus.append('<div class="inc ec_qtybtn">+</div>');
    $(".ec_qtybtn").on("click", function() {
        var $qtybutton = $(this);
        var QtyoldValue = $qtybutton.parent().find("input").val();
        if ($qtybutton.text() === "+") {
            var QtynewVal = parseFloat(QtyoldValue) + 1;
        } else {

            if (QtyoldValue > 1) {
                var QtynewVal = parseFloat(QtyoldValue) - 1;
            } else {
                QtynewVal = 1;
            }
        }
        $qtybutton.parent().find("input").val(QtynewVal);
    });

    /*--------------------- Product Countdown --------------------- */
    $("#ec-fs-count-1").countdowntimer({
        startDate : "2021/01/01 12:00:00",
        dateAndTime : "2021/10/10 12:00:00",
        labelsFormat : true,
        displayFormat : "DHMS"
    });

    $("#ec-fs-count-2").countdowntimer({
        startDate : "2021/01/01 12:00:00",
        dateAndTime : "2021/11/10 12:00:00",
        labelsFormat : true,
        displayFormat : "DHMS"
    });

    /*----------------------------- Feature Product Slider   -------------------------------- */
    $('.ec-exe-products').slick({
        rows: 1,
        dots: false,
        arrows: true,
        infinite: true,
        speed: 500,
        slidesToShow: 2,
        slidesToScroll: 1,
        responsive: [
        {
            breakpoint: 768,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 2,
            }
        },
        {
            breakpoint: 575,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 1,
            }
        }
        ]
    });

    /*-----------------------------  Offer Product Slider  -------------------------------- */
    $('.ec-spe-products').slick({
        rows: 1,
        dots: false,
        arrows: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1
    });

    /*----------------------------- Brand Slider -------------------------------- */    
    $('#ec-brand-slider').slick({
        rows: 1,
        dots: false,
        arrows: true,
        infinite: true,
        speed: 500,
        slidesToShow: 6,
        slidesToScroll: 1,
        responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 1,
                dots: false
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 1,
                dots: false
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToScroll: 3,
                slidesToShow: 2,
            }
        },
        {
            breakpoint: 400,
            settings: {
                slidesToScroll: 2,
                slidesToShow: 1,
            }
        }
        ]
    });

    /*----------------------------- All Product Slider -------------------------------- */    
    $('.ec-all-products .ec-new-slider,.ec-all-products .ec-special-slider,.ec-all-products .ec-best-slider').slick({
        rows: 4,
        dots: false,
        arrows: true,
        infinite: true,
        autoplay:false,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        },
        {
            breakpoint: 768,
            settings: {
                rows: 2,
                slidesToScroll: 2,
                slidesToShow: 2,
            }
        },
        {
            breakpoint: 480,
            settings: {
                rows: 2,
                slidesToScroll: 1,
                slidesToShow: 1,
            }
        }
        ]
    });

    /*----------------------------- Category Slider -------------------------------- */    
    $('.ec-category-section .ec_cat_slider').slick({
        rows: 1,
        dots: false,
        arrows: true,
        infinite: true,
        speed: 500,
        slidesToShow: 6,
        slidesToScroll: 1,
        responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 5
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 4
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 3
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 2,
            }
        }
        ]
    });

    /*----------------------------- Scroll Up Button --------------------- */
    $.scrollUp({
        scrollText: '<i class="ecicon eci-arrow-up" aria-hidden="true"></i>',
        easingType: "linear",
        scrollSpeed: 900,
        animation: "fade",
    });

    /*----------------------------- Theme Color Change -------------------------------- */
    $('.ec-change-color').on('click', 'li', function(){
        $('link[href^="assets/demo-5/css/skin-"]').remove();
        $('link.dark').remove();
        $('.ec-change-mode').removeClass("active");
        var dataValue = $(this).attr('data-color');

        if($(this).hasClass('active')) return;

        $(this).toggleClass('active').siblings().removeClass('active');

        if(dataValue != undefined){
            $("link[href='assets/demo-5/css/responsive.css']").before('<link rel="stylesheet" href="assets/demo-5/css/skin-'+dataValue+'.css" rel="stylesheet">');
            // localStorage.setItem("colormode", dataValue);
            ecCreateCookie('themeColorCookie',dataValue,1);
        }

        return false;
    });

    /*----------------------------- Theme RTL Change -------------------------------- */
    $(".ec-tools-sidebar .ec-change-rtl .ec-rtl-switch").click(function(e) {
        e.preventDefault();
        var $link = $('<link>', {
            rel: 'stylesheet',
            href: 'assets/demo-5/css/rtl.css',
            class: 'rtl'
        });
        $(this).parent().toggleClass('active');
        var rtlvalue = "ltr";
        if ($(this).parent().hasClass('ec-change-rtl') && $(this).parent().hasClass('active')){
            $link.appendTo('head');
            rtlvalue = "rtl";
            ecCreateCookie('rtlModeCookie',rtlvalue,1);
        } else if($(this).parent().hasClass('ec-change-rtl') && !$(this).parent().hasClass('active')){
            $('link.rtl').remove();
            rtlvalue = "ltr";
            ecDeleteCookie('rtlModeCookie',rtlvalue);
        }       
        // localStorage.setItem("rtlmode", rtlvalue);
    });

    /*----------------------------- Theme Dark mode Change -------------------------------- */
    $(".ec-tools-sidebar .ec-change-mode .ec-mode-switch").click(function(e) {
        e.preventDefault();
        var $link = $('<link>', {
            rel: 'stylesheet',
            href: 'assets/demo-5/css/dark.css',
            class: 'dark'
        });

        $(this).parent().toggleClass('active');
        var modevalue = "light";
        if ($(this).parent().hasClass('ec-change-mode') && $(this).parent().hasClass('active')){
                $("link[href='assets/demo-5/css/responsive.css']").before($link);

        } else if($(this).parent().hasClass('ec-change-mode') && !$(this).parent().hasClass('active')){
            $('link.dark').remove();
            modevalue = "light";
        }

        if ($(this).parent().hasClass('active')){
            $("#ec-fixedbutton .ec-change-color").css("pointer-events", "none");
            $("body").addClass("dark");
            modevalue = "dark";
            ecCreateCookie('darkModeCookie',modevalue,1);
        }else{
            $("#ec-fixedbutton .ec-change-color").css("pointer-events", "all");
            $("body").removeClass("dark");
            ecDeleteCookie('darkModeCookie',modevalue);
        }
        // localStorage.setItem("mode", modevalue);
    });    
   
    /*----------------------------- Full Screen mode Change -------------------------------- */   
    $(".ec-tools-sidebar .ec-fullscreen-mode .ec-fullscreen-switch").click(function(e) {
        e.preventDefault();
        
        $(this).parent().toggleClass('active');

        if (
            !document.fullscreenElement && // alternative standard method
            !document.mozFullScreenElement &&
            !document.webkitFullscreenElement &&
            !document.msFullscreenElement
        ) {
            // current working methods
            if (document.documentElement.requestFullscreen) {
                document.documentElement.requestFullscreen();
            } else if (document.documentElement.msRequestFullscreen) {
                document.documentElement.msRequestFullscreen();
            } else if (document.documentElement.mozRequestFullScreen) {
                document.documentElement.mozRequestFullScreen();
            } else if (document.documentElement.webkitRequestFullscreen) {
                document.documentElement.webkitRequestFullscreen(
                Element.ALLOW_KEYBOARD_INPUT
                );
            }
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            }
        }
    }); 
    
    /*----------------------------- Menu Active -------------------------------- */        
    var current_page_URL = location.href;
    $( ".ec-main-menu ul li a" ).each(function() {
        if ($(this).attr("href") !== "#") {
            var target_URL = $(this).prop("href");
            if (target_URL == current_page_URL) {
                $('.ec-main-menu a').parents('li, ul').removeClass('active');
                $(this).parent('li').addClass('active');
                return false;
            }
        }
    });

    /*----------------------------- Color Hover To Image Change -------------------------------- */ 
    var $ecproduct = $('.ec-product-tab,.ec-exe-products').find('.ec-opt-swatch');

    function initChangeImg($opt) {
        $opt.each(function() {
            var $this = $(this),
            ecChangeImg = $this.hasClass('ec-change-img');

            

            $this.on('mouseenter', 'li', function() {
                var $this = $(this);
                var $load = $(this).find('a');

                var $proimg = $this.closest('.ec-product-inner').find('.ec-pro-image');

                if (!$load.hasClass('loaded')) {
                    $proimg.addClass('pro-loading');
                }

                var $loaded = $(this).find('a').addClass('loaded');

                $this.addClass('active').siblings().removeClass('active');
                if (ecChangeImg) {
                    hoverAddImg($this);
                }
                setTimeout(function() {
                   $proimg.removeClass("pro-loading");
               }, 1000);
                return false;
            });


        });
    }

    function hoverAddImg($this) {
        var $optData = $this.find('.ec-opt-clr-img'),
        $opImg = $optData.attr('data-src'),
        $opImgHover = $optData.attr('data-src-hover') || false,
        $optImgWrapper = $this.closest('.ec-product-inner').find('.ec-pro-image'),
        $optImgMain = $optImgWrapper.find('.image img.main-image'),
        $optImgMainHover = $optImgWrapper.find('.image img.hover-image');

        if ($opImg.length) {
            $optImgMain.attr('src', $opImg);
        }
        if ($opImg.length) {
            var checkDisable = $optImgMainHover.closest('img.hover-image');
            $optImgMainHover.attr('src', $opImgHover);
            if (checkDisable.hasClass('disable')) {
                checkDisable.removeClass('disable');
            }
        }
        if ($opImgHover === false) {
            $optImgMainHover.closest('img.hover-image').addClass('disable');
        }
    }

    $(window).on('load', function() {
        initChangeImg($ecproduct);
    });

    $("document").ready(function(){
        initChangeImg($ecproduct);
    });

    /*----------------------------- Size Hover To Active -------------------------------- */
    $('.ec-opt-size').each(function() {
        $(this).on('mouseenter', 'li', function() {
            var $this = $(this);
            var $old_data =$this.find('a').attr('data-old');
            var $new_data =$this.find('a').attr('data-new');
            var $old_price = $this.closest('.ec-pro-content').find('.old-price');
            var $new_price = $this.closest('.ec-pro-content').find('.new-price');

            $old_price.text($old_data); 
            $new_price.text($new_data); 

            $this.addClass('active').siblings().removeClass('active');
        });
    });

    /*----------------------------- Replace all SVG images with inline SVG -------------------------------- */    
    $(document).ready(function() {
        $('img.svg_img[src$=".svg"]').each(function() {
            var $img = $(this);
            var imgURL = $img.attr('src');
            var attributes = $img.prop("attributes");

            $.get(imgURL, function(data) {
                    // Get the SVG tag, ignore the rest
                    var $svg = $(data).find('svg');

                    // Remove any invalid XML tags
                    $svg = $svg.removeAttr('xmlns:a');

                    // Loop through IMG attributes and apply on SVG
                    $.each(attributes, function() {
                        $svg.attr(this.name, this.value);
                    });

                    // Replace IMG with SVG
                    $img.replaceWith($svg);
                }, 'xml');
        });
    });

    /*----------------------------- Testimonial Slider -------------------------------- */    
    $(document).ready(function() {
        $('#ec-testimonial-slider').slick({
            centerMode: true,
            dots: true,
            arrows: false,
            infinite: true,
            speed: 500,
            slidesToShow: 3,
            slidesToScroll: 1,
            centerPadding: '0',
            responsive: [
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 1,
                    }
                }
            ]
        });
    });

    /*----------------------------- Footer Toggle -------------------------------- */    
    $(document).ready(function(){
        $("footer .footer-top .ec-footer-widget .ec-footer-links").addClass("ec-footer-dropdown");

        $('.ec-footer-heading').append( "<div class='ec-heading-res'><i class='ecicon eci-angle-down'></i></div>" );

        $(".ec-footer-heading .ec-heading-res").click(function() {
           var $this = $(this).closest('.footer-top .col-sm-12 .ec-footer-widget').find('.ec-footer-dropdown');
           $this.slideToggle('slow');
           $('.ec-footer-dropdown').not($this).slideUp('slow');
       });
    });

    /*----------------------------- Add To  Cart Toast -------------------------------- */    
    // $(document).ready(function(){
    //     $("button.add-to-cart").click(function() {
    //         $("#addtocart_toast").addClass("show");
    //         setTimeout(function(){ $("#addtocart_toast").removeClass("show") }, 3000);
    //     });
    //     $(".ec-btn-group.wishlist").click(function() {
    //         $("#wishlist_toast").addClass("show");
    //         setTimeout(function(){ $("#wishlist_toast").removeClass("show") }, 3000);
    //     });
    // });

    $(document).ready(function(){
        $('.ec-pro-image').append( "<div class='ec-pro-loader'></div>" );
    });

    function contentheight() {
        $('.ec-product-content .pro-hidden-block').each(function(){ 

            var $hover = $(this).closest(".ec-product-inner").find(".ec-product-hover");
            var $option = $(this).closest(".ec-product-inner").find(".ec-pro-option");
            
             $hover.css({
                'margin-bottom' : - ($(this).outerHeight() + $option.outerHeight()) + 'px'
            });
        });
    }

    $(window).on('load', function() {
        contentheight();
    });

    $(window).on('resize', function() {
        contentheight();
    });

    $("document").ready(function(){
        contentheight();
    });

    /*----------------------------- bg skin ---------------------- */
    (function () {
        $().appendTo($('body'));
    })();

    $(".bg-option-box").on("click", function (e) {
        e.preventDefault();
        if ($(this).hasClass("in-out")) {
            $(".bg-switcher").stop().animate({ right: "0px" }, 100);
            if ($(".color-option-box").not("in-out")) {
                $(".skin-switcher").stop().animate({ right: "-163px" }, 100);
                $(".color-option-box").addClass("in-out");
            }
            if ($(".layout-option-box").not("in-out")) {
                $(".layout-switcher").stop().animate({ right: "-163px" }, 100);
                $(".layout-option-box").addClass("in-out");
            }
        } else {
            $(".bg-switcher").stop().animate({ right: "-163px" }, 100);
        }

        $(this).toggleClass("in-out");
        return false;
    });

    /*----------------------------- bg Image ---------------------- */
    $('.back-bg-1').on('click', function (e) {
        var bgID = $(this).attr("id");
        var bgClass = "body-bg-1";
        setBGImage(bgID, bgClass);
    });

    $('.back-bg-2').on('click', function (e) {
        var bgID = $(this).attr("id");
        var bgClass = "body-bg-2";
        setBGImage(bgID, bgClass);
    });

    $('.back-bg-3').on('click', function (e) {
        var bgID = $(this).attr("id");
        var bgClass = "body-bg-3";
        setBGImage(bgID, bgClass);
    });

    $('.back-bg-4').on('click', function (e) {
        var bgID = $(this).attr("id");
        var bgClass = "body-bg-4";
        setBGImage(bgID, bgClass);
    });

    function setBGImage(bgID, bgClass) {
        $("body").removeClass("body-bg-1");
        $("body").removeClass("body-bg-2");
        $("body").removeClass("body-bg-3");
        $("body").removeClass("body-bg-4");

        $("body").addClass(bgClass);

        $("#bg-switcher-css").attr("href", "assets/demo-5/css/backgrounds/" + bgID + ".css");

        var bgIDClass = bgID + '||' + bgClass;

        ecCreateCookie('bgImageModeCookie', bgIDClass, 1);
    }

    /*----------------------------- Language select options google translate ---------------------- */
    $(".lang-option-box").on("click", function (e) {
        e.preventDefault();
        if ($(this).hasClass("in-out")) {
            $(".lang-switcher").stop().animate({ right: "0px" }, 100);
            if ($(".color-option-box").not("in-out")) {
                $(".skin-switcher").stop().animate({ right: "-163px" }, 100);
                $(".color-option-box").addClass("in-out");
            }
            if ($(".layout-option-box").not("in-out")) {
                $(".layout-switcher").stop().animate({ right: "-163px" }, 100);
                $(".layout-option-box").addClass("in-out");
            }
        } else {
            $(".lang-switcher").stop().animate({ right: "-163px" }, 100);
        }

        $(this).toggleClass("in-out");
        return false;
    });

    /*----------------------------- Tools sidebar ---------------------- */
    $(".ec-tools-sidebar-toggle").on("click", function (e) {
        e.preventDefault();
        if ($(this).hasClass("in-out")) {
            $(".ec-tools-sidebar").stop().animate({ right: "0px" }, 100);
            $(".ec-tools-sidebar-overlay").fadeIn();
            if ($(".ec-tools-sidebar-toggle").not("in-out")) {
                $(".ec-tools-sidebar").stop().animate({ right: "-280px" }, 100);
                $(".ec-tools-sidebar-toggle").addClass("in-out");
                // $(".ec-tools-sidebar-overlay").fadeOut();
            }
            if ($(".ec-tools-sidebar-toggle").not("in-out")) {
                $(".ec-tools-sidebar").stop().animate({ right: "0" }, 100);
                $(".ec-tools-sidebar-toggle").addClass("in-out");
                $(".ec-tools-sidebar-overlay").fadeIn();
            }
        } else {
            $(".ec-tools-sidebar").stop().animate({ right: "-280px" }, 100);
            $(".ec-tools-sidebar-overlay").fadeOut();
        }

        $(this).toggleClass("in-out");
        return false;
    });

    $(".ec-tools-sidebar-overlay").on("click", function (e) {
        $(".ec-tools-sidebar-toggle").addClass("in-out");
        $(".ec-tools-sidebar").stop().animate({ right: "-280px" }, 100);
        $(".ec-tools-sidebar-overlay").fadeOut();
    });

    /*----------------------------- Instagram slider & Category slider & Tooltips -----------------------------------*/
    $(function(){

        $('.insta-auto').infiniteslide({
            direction: 'left',
            speed: 50,
            clone: 10
        });

        $('[data-toggle="tooltip"]').tooltip();
    });

})(jQuery);


