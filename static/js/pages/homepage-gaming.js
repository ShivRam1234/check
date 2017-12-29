
jQuery(function($){
   "use strict";

   var SLZ = window.SLZ || {};


   /*=======================================
   =             MAIN FUNCTION             =
   =======================================*/

   SLZ.homepageGaming = function(){
        $('.slider-for-1-item').slick({
          slidesToShow: 1,
          slidesToScroll: 1,
          draggable: false,
          arrows: false,
          fade: true,
          asNavFor: '.slider-nav-1-item'
        });        
        $('.slider-nav-1-item').slick({
            infinite: true,
            loop: true,
            slidesToShow: 4,
            slidesToScroll: 1,
            asNavFor: '.slider-for-1-item',
            dots: false,
            arrows: false,
            focusOnSelect: true,
            responsive: [
                {
                    breakpoint: 1025,
                    settings: {
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 2
                    }
                },
                {
                    breakpoint: 481,
                    settings: {
                        slidesToShow: 1
                    }
                }
            ]
        });

        $('.slider-for-1-item-sidebar').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            draggable: false,
            arrows: false,
            fade: true,
            asNavFor: '.slider-nav-1-item-sidebar'
        });        
        $('.slider-nav-1-item-sidebar').slick({
            infinite: true,
            loop: true,
            slidesToShow: 4,
            slidesToScroll: 1,
            asNavFor: '.slider-for-1-item-sidebar',
            dots: false,
            arrows: true,
            focusOnSelect: true,
            responsive: [
                {
                    breakpoint: 1025,
                    settings: {
                        arrows: false
                    }
                },
                {
                    breakpoint: 769,
                    settings:  {
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 601,
                    settings:  {
                        slidesToShow: 2
                    }
                }
            ]
        });    

        $('.slick-4-item-couple').slick({
            dots: false,
            arrows: false,
            infinite: true,
            speed: 500,
            slidesToShow: 4,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 1025,
                    settings: {
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 2
                    }
                },
                {
                    breakpoint: 481,
                    settings: {
                        slidesToShow: 1
                    }
                }
            ]
        });   

        $(".middle-banner-slider .comment-contain-scrollbar").mCustomScrollbar({
            theme: "light",
            autoHideScrollbar: true
        });

        autosize($('textarea'));
   };


   /*======================================
   =            INIT FUNCTIONS            =
   ======================================*/

   $(document).ready(function(){
       SLZ.homepageGaming();
   });

   /*======================================
   =          END INIT FUNCTIONS          =
   ======================================*/

});