;(function($){
    "use strict"
	
	
	var nav_offset_top = $('header').height() + 50; 
    /*-------------------------------------------------------------------------------
	  Navbar 
	-------------------------------------------------------------------------------*/

	//* Navbar Fixed  
    function navbarFixed(){
        if ( $('.header_area').length ){ 
            $(window).scroll(function() {
                var scroll = $(window).scrollTop();   
                if (scroll >= nav_offset_top ) {
                    $(".header_area").addClass("navbar_fixed");
                } else {
                    $(".header_area").removeClass("navbar_fixed");
                }
            });
        };
    };
    navbarFixed();
	
	
	/*----------------------------------------------------*/
    /*  Parallax Effect js
    /*----------------------------------------------------*/
	function parallaxEffect() {
    	$('.bg-parallax').parallax();
	}
	parallaxEffect();
	
	
//	$('.courses_area').imagesLoaded(function(){
//        $('.courses_inner').isotope({ 
//            layoutMode: 'masonry',
//			percentPosition: true,
//			masonry: {
//				columnWidth: 1,
//			}
//        })
//    });
	
	
	
	
	/*----------------------------------------------------*/
    /*  portfolio_isotope
    /*----------------------------------------------------*/
   
//	$('.courses_inner').imagesLoaded(function(){
//        $('.courses_inner').isotope({ 
//            layoutMode: 'masonry',
//            percentPosition:true,
//            masonry: {
//                columnWidth: 1,
//            }            
//        })
//    });
	
	
	/*----------------------------------------------------*/
    /*  Clients Slider
    /*----------------------------------------------------*/
//    function clients_slider(){
//        if ( $('.clients_slider').length ){
//            $('.clients_slider').owlCarousel({
//                loop:true,
//                margin: 30,
//                items: 5,
//                nav: false,
//                autoplay: false,
//                smartSpeed: 1500,
//                dots:false, 
//                responsiveClass: true,
//                responsive: {
//                    0: {
//                        items: 1,
//                    },
//                    400: {
//                        items: 2,
//                    },
//                    575: {
//                        items: 3,
//                    },
//                    768: {
//                        items: 4,
//                    },
//                    992: {
//                        items: 5,
//                    }
//                }
//            })
//        }
//    }
//    clients_slider();
	/*----------------------------------------------------*/
    /*  MailChimp Slider
    /*----------------------------------------------------*/
    
	
	/*----------------------------------------------------*/
    /*  Simple LightBox js
    /*----------------------------------------------------*/
    $('.imageGallery1 .light').simpleLightbox();
	
	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});
	
	// 상단 메뉴바
	$(".skill_main").each(function() {
        $(this).waypoint(function() {
            var progressBar = $(".progress-bar");
            progressBar.each(function(indx){
                $(this).css("width", $(this).attr("aria-valuenow") + "%")
            })
        }, {
            triggerOnce: true,
            offset: 'bottom-in-view'

        });
    });
	
	/*----------------------------------------------------*/
    /*  Isotope Fillter js 갤러리 애니메이션
    /*----------------------------------------------------*/
	function gallery_isotope(){
        if ( $('.gallery_f_inner').length ){
            // Activate isotope in container
			$(".gallery_f_inner").imagesLoaded( function() {
                $(".gallery_f_inner").isotope({
                    layoutMode: 'fitRows',
                    animationOptions: {
                        duration: 750,
                        easing: 'linear'
                    }
                }); 
            });
			
            // Add isotope click function
            $(".gallery_filter li").on('click',function(){
                $(".gallery_filter li").removeClass("active");
                $(this).addClass("active");

                var selector = $(this).attr("data-filter");
                $(".gallery_f_inner").isotope({
                    filter: selector,
                    animationOptions: {
                        duration: 450,
                        easing: "linear",
                        queue: false,
                    }
                });
                return false;
            });
        }
    }
    gallery_isotope();
	
	/*----------------------------------------------------*/
    /*  Testimonials Slider
    /*----------------------------------------------------*/
    
	
	/*----------------------------------------------------*/
    /*  Google map js
    /*----------------------------------------------------*/
    

})(jQuery)