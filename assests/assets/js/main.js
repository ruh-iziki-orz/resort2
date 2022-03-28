/**
 * Template Name: EstateAgency - v4.7.0
 * Template URL: https://bootstrapmade.com/real-estate-agency-bootstrap-template/
 * Author: BootstrapMade.com
 * License: https://bootstrapmade.com/license/
 */




 

 $('body').on('click tap', 'button#menu-toggle', function(){
	$('header').addClass('active');
});

$('body').click(function(e){
	if(!$(e.target).is('button#menu-toggle')) {
   	$('header').removeClass('active');
			$('div.menu-panel').removeClass('is-active');
   }
});

$('nav.slide-out-menu').click(function(e){
	e.stopPropagation();
});

$('button.menu-link').click(function(){
		$('div.menu-panel').removeClass('is-active');

	if ($(this).data('ref')) {
		var targetRef = $(this).data('ref');
		var $target = $('div.menu-panel[data-menu="' + targetRef + '"]');
		
			$target.addClass('is-active');
	}
});


var acc = document.getElementsByClassName("accordion");
var i;


console.log("hello")
const region_dropdown=document.getElementById("region")
const area_dropdown=document.getElementById('area')
region_dropdown.addEventListener('change',e=>{
    selected=e.target.value
   
    console.log(selected)
    $.ajax({
        type:'GET',
        url:`/areas/${selected}`,
        success:function(response){
            console.log(response.data)
            area_dropdown.innerHTML=""
            const option=document.createElement('option')
            option.textContent='all'
            option.setAttribute('value',-1)
            area_dropdown.appendChild(option)
            const areas_data=response.data
            areas_data.map(item=>{
               
                option.textContent=item.name
                option.setAttribute('value',item.id)
                area_dropdown.appendChild(option)
            })
        },
    }) 
})



for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}



(function() {
    "use strict";

    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
        el = el.trim()
        if (all) {
            return [...document.querySelectorAll(el)]
        } else {
            return document.querySelector(el)
        }
    }

    /**
     * Easy event listener function
     */
    const on = (type, el, listener, all = false) => {
        let selectEl = select(el, all)
        if (selectEl) {
            if (all) {
                selectEl.forEach(e => e.addEventListener(type, listener))
            } else {
                selectEl.addEventListener(type, listener)
            }
        }
    }

    /**
     * Easy on scroll event listener 
     */
    const onscroll = (el, listener) => {
        el.addEventListener('scroll', listener)
    }

    /**
     * Toggle .navbar-reduce
     */
    let selectHNavbar = select('.navbar-default')
    if (selectHNavbar) {
        onscroll(document, () => {
            if (window.scrollY > 100) {
                selectHNavbar.classList.add('navbar-reduce')
                selectHNavbar.classList.remove('navbar-trans')
            } else {
                selectHNavbar.classList.remove('navbar-reduce')
                selectHNavbar.classList.add('navbar-trans')
            }
        })
    }

    /**
     * Back to top button
     */
    let backtotop = select('.back-to-top')
    if (backtotop) {
        const toggleBacktotop = () => {
            if (window.scrollY > 100) {
                backtotop.classList.add('active')
            } else {
                backtotop.classList.remove('active')
            }
        }
        window.addEventListener('load', toggleBacktotop)
        onscroll(document, toggleBacktotop)
    }



    /**
     * Preloader
     */
    let preloader = select('#preloader');
    if (preloader) {
        window.addEventListener('load', () => {
            preloader.remove()
        });
    }

    /**
     * Search window open/close
     */
    let body = select('body');
    on('click', '.navbar-toggle-box', function(e) {
        e.preventDefault()
        body.classList.add('box-collapse-open')
        body.classList.remove('box-collapse-closed')
    })

    on('click', '.close-box-collapse', function(e) {
            e.preventDefault()
            body.classList.remove('box-collapse-open')
            body.classList.add('box-collapse-closed')
        })
        /**
         * Intro Carousel
         */
    new Swiper('.intro-carousel', {
        speed: 600,
        loop: true,
        autoplay: {
            delay: 2000,
            disableOnInteraction: false
        },
        slidesPerView: 'auto',
        pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true
        }
    });

    /**
     * Property carousel
     */
    new Swiper('#property-carousel', {
        speed: 600,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false
        },
        slidesPerView: 'auto',
        pagination: {
            el: '.propery-carousel-pagination',
            type: 'bullets',
            clickable: true
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 20
            },

            1200: {
                slidesPerView: 3,
                spaceBetween: 20
            }
        }
    });

    /**
     * News carousel
     */
    new Swiper('#news-carousel', {
        speed: 600,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false
        },
        slidesPerView: 'auto',
        pagination: {
            el: '.news-carousel-pagination',
            type: 'bullets',
            clickable: true
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 20
            },

            1200: {
                slidesPerView: 3,
                spaceBetween: 20
            }
        }
    });

    /**
     * Testimonial carousel
     */
    new Swiper('#testimonial-carousel', {
        speed: 600,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false
        },
        slidesPerView: 'auto',
        pagination: {
            el: '.testimonial-carousel-pagination',
            type: 'bullets',
            clickable: true
        }
    });

    /**
     * Property Single carousel
     */
    new Swiper('#property-single-carousel', {
        speed: 600,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false
        },
        pagination: {
            el: '.property-single-carousel-pagination',
            type: 'bullets',
            clickable: true
        }
    });

})()