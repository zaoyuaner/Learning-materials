$(function () {
        $.getJSON('/wheel/', function (response_data) {
            var $swiperwrapper = $('#banner .swiper-wrapper')
            for (var i = 0; i < response_data['wheels'].length; i++) {
                var $slide = $('<div class="swiper-slide"></div>')
                    .appendTo($swiperwrapper)
                $('<img>').attr('src', response_data['wheels'][i].img).appendTo($slide)
            }
            var swiper = new Swiper('.swiper-container', {
                pagination: '.swiper-pagination',
                nextButton: '.swiper-button-next',
                prevButton: '.swiper-button-prev',
                paginationClickable: true,
                spaceBetween: 30,
                centeredSlides: true,
                autoplay: 2500,
                autoplayDisableOnInteraction: false
            });
        })


        $.getJSON('/goods/', function (response_data) {
            console.log(response_data['goods'][0].img)
            var $msb = $('#msb-wo-list ul')
            for (var i = 0; i < response_data['goods'].length; i++) {
                var $li = $('<li></li>').appendTo($msb)
                var $a = $('<a></a>').appendTo($li)

                $('<img>').attr('src', response_data['goods'][i].img).appendTo($a)
               var $p =  $('<p></p>').appendTo($a)
                $p.html(response_data['goods'][i].name)
                var $span =  $('<span></span>').appendTo($a)
                $span.text('￥ ' + response_data['goods'][i].price)

            }
        })

    }
)
