jQuery(function($) {
    "use strict";

    var SLZ = window.SLZ || {};

    /*=======================================
    =             MAIN FUNCTION             =
    =======================================*/

    SLZ.mainFunction = function() {

        // Isotope
        var $grid = $('.news-masonry');
        $grid.isotope({
            itemSelector: '.masonry-item-wrapper',
            layoutMode: 'masonry',
            percentPosition: true,
            masonry: {
                columnWidth: '.item-width-1'
            }

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
