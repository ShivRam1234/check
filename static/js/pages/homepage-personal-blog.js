jQuery(function($) {
    "use strict";

    var SLZ = window.SLZ || {};

    /*=======================================
    =             MAIN FUNCTION             =
    =======================================*/
    function shorttext() {
        var label_height = $('.banner-slide-homepersonalblog .slick-current .label-wrapper').height(),
        title_height = $('.banner-slide-homepersonalblog .slick-current .title').height(),
        blockquote_height = $('.banner-slide-homepersonalblog .slick-current blockquote').outerHeight(true),
        readmore_height = $('.banner-slide-homepersonalblog .slick-current .read-more').outerHeight(true);
        if(window.innerWidth > 1024) {
            $('.banner-slide-homepersonalblog .slick-current .more-text').css('max-height', $('.banner-slide-homepersonalblog .slick-current .news-image').height() - 92 - label_height - blockquote_height - title_height - readmore_height);
        }
        else {
            $('.banner-slide-homepersonalblog .slick-current .more-text').css('max-height', $('.banner-slide-homepersonalblog .slick-current .news-image').height() - 68 - label_height - blockquote_height - title_height - readmore_height);
        }
    }

    function arrow_position() {
        if(window.innerWidth > 767)
            $('.banner-slide-homepersonalblog .slick-prev, .banner-slide-homepersonalblog .slick-next').css({
                'left': $('.banner-slide-homepersonalblog .slick-slide.slick-current.slick-active .news-image').width()-$('.banner-slide-homepersonalblog .slick-prev').width(),
                'right': 'auto',
            });
        else
            $('.banner-slide-homepersonalblog .slick-prev, .banner-slide-homepersonalblog .slick-next').css({
                'top': $('.banner-slide-homepersonalblog .slick-slide.slick-current.slick-active .news-image').height()-$('.banner-slide-homepersonalblog .slick-prev').height(),
            });
    }

    SLZ.mainFunction = function() {

        // Slide Main Banner
        $('.slider-for').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            fade: true,
            asNavFor: '.slider-nav',
            dots: false,
            arrows: true,
            speed: 500,
            draggable: false,
            adaptiveHeight: true,

        });
        $('.slider-nav').slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            asNavFor: '.slider-for',
            adaptiveHeight: true,
            arrows: false,
            dots: true,
            focusOnSelect: true,
            responsive: [
                {
                    breakpoint: 1025,
                    settings: {
                        slidesToShow: 3,
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 481,
                    settings: {
                        slidesToShow: 1,
                    }
                }
            ]
        });

        $('.banner-slide-homepersonalblog .slider-nav').on('swipe', function(event, slick, direction) {
            if(window.innerWidth > 768)
                shorttext();
        });
        $('.banner-slide-homepersonalblog .slider-nav').on('afterChange', function(event, slick, currentSlide){
            if(window.innerWidth > 768)
                shorttext();
        });


        $('.banner-slide-homepersonalblog .slick-arrow').on('click', function(event) {
            $('.banner-slide-homepersonalblog .list-items').slick('setPosition');

            setTimeout(function() {
                $(".banner-slide-homepersonalblog").removeClass("loaded");
            },1000);

            setTimeout(function() {
                if(window.innerWidth > 768)
                    shorttext();

                arrow_position();
            },600);
        });
    };


    /*======================================
    =            INIT FUNCTIONS            =
    ======================================*/

    $(document).ready(function() {
        SLZ.mainFunction();
    });

    /*=====  End of INIT FUNCTIONS  ======*/

    $(window).on('load resize', function() {

        setTimeout(function() {
            if(window.innerWidth > 768)
                shorttext();
            $('.banner-slide-homepersonalblog .list-items').slick('setPosition');

            arrow_position();

            if(window.innerWidth > 767)
                $('.banner-slide-homepersonalblog .slider-for,.banner-slide-homepersonalblog .news-layout-4').css('height', $('.banner-slide-homepersonalblog .slick-current .news-image').height());
            else
                $('.banner-slide-homepersonalblog .news-layout-4').css('height', 'auto');
        },400);
    });
});
