
jQuery(function($){
   "use strict";

   var SLZ = window.SLZ || {};


   /*=======================================
   =             MAIN FUNCTION             =
   =======================================*/

   SLZ.mainFunction = function(){

        // Slide Main Banner 
        $('.banner-slide-homecenter .list-items').slick({
            dots: false,
            arrows: true,
            infinite: true,
            speed: 500,
            autoplaySpeed: 4000,
            slidesToShow: 1,
            centerMode: true,
            centerPadding: '22%',
            responsive: [
                {
                    breakpoint: 1025,
                    settings: {
                        centerPadding: '15%',
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        centerPadding: '70px',
                    }
                },
                {
                    breakpoint: 481,
                    settings: {
                        arrows: false,
                        centerPadding: '15px',
                    }
                }
            ]
        });



        // slide gallery
        $('.gallery-slick-wrapper .slider-for').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: true,
            fade: true,
            asNavFor: '.gallery-slick-wrapper .slider-nav'
        });

        $('.gallery-slick-wrapper .slider-nav').slick({
            slidesToShow: 6,
            slidesToScroll: 1,
            asNavFor: '.gallery-slick-wrapper .slider-for',
            focusOnSelect: true,
            arrows: false,
            responsive: [
                {
                    breakpoint: 1025,
                    settings: {
                        slidesToShow: 5
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 5
                    }
                },
                {
                    breakpoint: 601,
                    settings: {
                        slidesToShow: 4
                    }
                },
                {
                    breakpoint: 415,
                    settings: {
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 381,
                    settings: {
                        slidesToShow: 2
                    }
                }
            ]
        });

        // slide news - owlcarousel
        var news_with_sidebar = $('.banner-news-wrapper .main-slide');
        news_with_sidebar.owlCarousel({
            loop: true,
            margin: 0,
            nav: true,
            dots: true,
            animateIn: 'fadeIn',
            animateOut: 'fadeOut',
            autoplay: true,
            autoplayTimeout: 6000,
            autoplaySpeed: 1000,
            smartSpeed: 1000,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right" ></i>'],
            items: 1
        });

        //set active for news list
        news_with_sidebar.on("changed.owl.carousel", function(event) {
            var current = event.item.index;
            var datasrc = $(event.target).find('.owl-item').eq(current).find('.item').attr('data-item');
            //console.log(datasrc);
            $('.banner-news-wrapper .slide-items li').removeClass('active');
            $('.banner-news-wrapper .slide-items li.' + datasrc).addClass('active');
            if($('.banner-news-wrapper .slide-items li.active').is('li:first-child')) {
                $('.banner-news-wrapper .slide-items').mCustomScrollbar('scrollTo','top');
            }
            else
                $('.banner-news-wrapper .slide-items').mCustomScrollbar('scrollTo',
                    '-='+$('.banner-news-wrapper .slide-items li.active').prev().outerHeight(true));
        });
        //set active when click item
        $('.banner-news-wrapper .slide-items li').each(function(index) {
            $(this).click(function(event) {
                var xlenght = $('.banner-news-wrapper .owl-dots .owl-dot').length;
                var key = $(this).index();
                //console.log(key);
                $('.banner-news-wrapper .owl-dots .owl-dot').eq(key).click();
            });
        });
   };

   SLZ.resizeFunction = function() {
        if($('.banner-news-wrapper .main-news').length > 0 ) {
            var xh=$('.banner-news-wrapper .main-news').height();
            $('.banner-news-wrapper .title-news ul').css('height', xh - $('.banner-news-wrapper .title-news > div').outerHeight(true) );
        }
    };

   /*======================================
   =            INIT FUNCTIONS            =
   ======================================*/

   $(document).ready(function(){
       SLZ.mainFunction();
   });

   $(window).on('resize load', function() {
        SLZ.resizeFunction();
    });

   /*======================================
   =          END INIT FUNCTIONS          =
   ======================================*/

});