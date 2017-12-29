
jQuery(function($){
   "use strict";

   var SLZ = window.SLZ || {};


   /*=======================================
   =             MAIN FUNCTION             =
   =======================================*/

   SLZ.singlepostFunction = function(){
       $('.button-more').on('click', function () {
           $('.item.other-share-wrapper').toggleClass('activeOtherShare');
           $('.button-more .ic-more').toggleClass('hide');
           $('.button-more .share-text.more').toggleClass('hide');
           $('.button-more .ic-less').toggleClass('hide');
           $('.button-more .share-text.less').toggleClass('hide');
       });
   };

   /*======================================
   =            INIT FUNCTIONS            =
   ======================================*/

   $(document).ready(function(){
       SLZ.singlepostFunction();
   });

   /*======================================
   =          END INIT FUNCTIONS          =
   ======================================*/

});

// Animate the element's value from x to y:
$({ someValue: 0 }).animate({ someValue: Math.floor(Math.random() * 3000) }, {
    duration: 3000,
    easing: 'swing', // can be anything
    step: function () { // called on every step
        // Update the element's text with rounded-up value:
        $('.count').text(commaSeparateNumber(Math.round(this.someValue)));
    }
});

function commaSeparateNumber(val) {
    while (/(\d+)(\d{3})/.test(val.toString())) {
        val = val.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
    }
    return val;
}