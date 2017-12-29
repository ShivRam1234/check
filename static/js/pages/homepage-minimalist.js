jQuery(function($) {
    "use strict";

    var SLZ = window.SLZ || {};

    /*=======================================
    =             MAIN FUNCTION             =
    =======================================*/

    function shorttext() {
        var label_height = $('.banner-slide-homeminimalist .list-items .label-wrapper').height(),
        title_height = $('.banner-slide-homeminimalist .list-items .title').outerHeight(true),
        blockquote_height = $('.banner-slide-homeminimalist blockquote').outerHeight(true),
        readmore_height = $('.banner-slide-homeminimalist .list-items .read-more').outerHeight(true);
        if(window.innerWidth > 1024) {
            $('.banner-slide-homeminimalist .list-items .more-text').css('max-height', $('.banner-slide-homeminimalist .list-items .news-image').height() - parseInt($('.banner-slide-homeminimalist .list-items .news-content').css('padding-top'),10) + 13 - 48 - label_height - blockquote_height - title_height - readmore_height);
        }
        else {
            $('.banner-slide-homeminimalist .list-items .more-text').css('max-height', $('.banner-slide-homeminimalist .list-items .news-image').height() - parseInt($('.banner-slide-homeminimalist .list-items .news-content').css('padding-top'),10) - 48 - label_height - blockquote_height - title_height - readmore_height);
        }
    }

    function arrow_position() {
        if(window.innerWidth > 767)
            $('.banner-slide-homeminimalist .slick-prev, .banner-slide-homeminimalist .slick-next').css({
                'left': $('.banner-slide-homeminimalist .slick-slide.slick-current.slick-active .news-image img').width()-$('.banner-slide-homeminimalist .slick-prev').width(),
                'right': 'auto',
            });
        else
            $('.banner-slide-homeminimalist .slick-prev, .banner-slide-homeminimalist .slick-next').css({
                'top': $('.banner-slide-homeminimalist .slick-slide.slick-current.slick-active .news-image img').height()-$('.banner-slide-homeminimalist .slick-prev').height(),
            });
    }

    SLZ.mainFunction = function() {
        var get_first_item = $('.banner-slide-homeminimalist .list-items-2 > div:first-child');
        $('.banner-slide-homeminimalist .list-items-2 > div:first-child').remove();
        $('.banner-slide-homeminimalist .list-items-2').append(get_first_item);
        // Slide Main Banner
        $('.banner-slide-homeminimalist .list-items').slick({
            dots: false,
            arrows: true,
            speed: 520,
            draggable: false,
            autoplaySpeed: 4000,
            slidesToShow: 1,
            responsive: [
                {
                    breakpoint: 668,
                    settings: {
                        adaptiveHeight: true,
                    }
                },
            ]
        });

        $('.banner-slide-homeminimalist .list-items-2').slick({
            dots: false,
            arrows: false,
            speed: 500,
            draggable: false,
            focusOnSelect: true,

            autoplaySpeed: 4000,
            slidesToShow: 1,
        });
        $('.banner-slide-homeminimalist .slick-arrow').addClass('waiting');
        setTimeout(function() {
            $('.banner-slide-homeminimalist .slick-arrow').removeClass('waiting');
        },600);

        $('.banner-slide-homeminimalist .slick-arrow').on('click', function(event) {
            $('.banner-slide-homeminimalist .slick-arrow').addClass('waiting');
            setTimeout(function() {
                if(window.innerWidth > 768)
                    shorttext();

                arrow_position();

                $('.banner-slide-homeminimalist .slick-arrow').removeClass('waiting');

            },400);
        });

        $('.banner-slide-homeminimalist .slick-next').on('click', function(event) {
            $('.banner-slide-homeminimalist .slick-slider').slick('slickNext');
        });

        $('.banner-slide-homeminimalist .slick-prev').on('click', function(event) {
            $('.banner-slide-homeminimalist .slick-slider').slick('slickPrev');
        });

        $('.banner-slide-homeminimalist .list-items-2').on('click', function(event) {
            $('.banner-slide-homeminimalist .slick-slider').slick('slickNext');
            
            $('.banner-slide-homeminimalist .slick-arrow').addClass('waiting');
            setTimeout(function() {
                if(window.innerWidth > 768)
                    shorttext();

                arrow_position();

                $('.banner-slide-homeminimalist .slick-arrow').removeClass('waiting');

            },400);
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
            arrow_position();
            if(window.innerWidth > 768)
                shorttext();
        },400);


        // Equal height for column
        if(window.innerWidth > 767) {
            var heights = $('.equal-height > div').map(function() {
                return $(this).height();
            }).get(),

            maxHeight = Math.max.apply(null, heights);
            $('.equal-height > div').height(maxHeight);
        }
    });


});
