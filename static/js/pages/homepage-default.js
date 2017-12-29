jQuery(function($) {
    "use strict";

    var SLZ = window.SLZ || {};

    /*=======================================
    =             MAIN FUNCTION             =
    =======================================*/

    SLZ.mainFunction = function() {

        // Slide Main Banner 
        $('.banner-slide-homepage .list-items').slick({
            dots: false,
            arrows: false,
            infinite: true,
            speed: 500,
            autoplaySpeed: 4000,
            slidesToShow: 1,
            adaptiveHeight: true,
        });

    };


    /*======================================
    =            INIT FUNCTIONS            =
    ======================================*/

    $(document).ready(function() {
        SLZ.mainFunction();
    });

    /*=====  End of INIT FUNCTIONS  ======*/

    $(window).on('load', function() {
        
    });

    
});
