/**
 * Created by Administrator on 2017/11/8.
 */
 $(function () {
    $(".item_title").click(function () {
        $(this).next().toggleClass("hide")
    })
})

