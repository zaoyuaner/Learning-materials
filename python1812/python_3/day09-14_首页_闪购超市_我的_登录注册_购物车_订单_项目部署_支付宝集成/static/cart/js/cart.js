$(function () {
    $('.cart').width(innerWidth)

    total()

    // 选中处理
    $('.cart .confirm-wrapper').click(function () {

        var $span = $(this).find('span')

        request_data = {
            'cartid':$(this).attr('data-cardid')
        }

        $.get('/axf/changecartselect/', request_data, function (response) {
            console.log(response)

            if (response.status == 1) {
                if (response.isselect){
                    $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                } else {
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                }

                total()
            }
        })
    })


    // 全选/取消全选
    $('.cart .all').click(function () {
        var isall = $(this).attr('data-all')
        $span = $(this).find('span')

        // 点击后去反
        isall = (isall == 'false') ? true : false

        // 记录
        $(this).attr('data-all', isall)

        if (isall){
            $span.removeClass('no').addClass('glyphicon glyphicon-ok')
        } else {
            $span.removeClass('glyphicon glyphicon-ok').addClass('no')
        }

        request_data = {
            'isall':isall
        }

        $.get('/axf/changecartall/', request_data, function (response) {
            console.log(response)

            if (response.status == 1){
                $('.confirm-wrapper').each(function () {
                    if (isall){ // 全选
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    } else {    // 取消全选
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }

                    total()
                })
            }
        })
    })
    
    
    // 计算总数
    function total() {
        var sum = 0

        // 遍历 获取 选中
        $('.cart li').each(function () {
            var $confirm = $(this).find('.confirm-wrapper')
            var $content = $(this).find('.content-wrapper')

            // 选中状态
            if ($confirm.find('.glyphicon').length){
                var price = $content.find('.price').attr('data-price')
                var num = $content.find('.num').attr('data-number')

                sum += num * price
            }
        })

        // 显示
        $('.bill .total b').html(sum)
    }

    // 下单
    // $('#order').click(function () {
    //     $.get('/axf/generateorder/', function (response) {
    //         console.log(response)
    //
    //         // 跳转
    //     })
    // })
})