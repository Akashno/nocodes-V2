$(function(){
    $('.blog-moto,.post-title').fadeIn(1000);
    setTimeout(function(){
        $('.blog-moto,.post-title').fadeOut(1000, function(){
            location.reload(true);
        });
    }, 60000);
});