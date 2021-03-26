
$('#search').on('input',function(){
    $.ajax({
        type:"POST",
        url:"",
        data:{
            text :$('#search').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success:function(data){

        var posts = $.parseJSON(data.posts);
        $("#blog-wrapper").empty();
        $('.result').empty();

        if (Object.keys(posts).length === 0)
        {
            $(".result").append('<div class="row"><div class="col-md-2 col-sm-0"></div><div class="col-md-8 col-sm-12 "><h6 class=" px-5  mt-4 text-secondary"> No blogs available as per your search</h6></div><div class="col-md-2 col-sm-0"></div></div>');
         };

        for(var prop in posts) {
            var item = posts[prop];

             $("#blog-wrapper").append('<div class="row mb-2"><div class="col-md-4 col-12 order-lg-1 order-md-1 order-2"><div class="container-fluid author-container  ml-3 "><div class="row mb-0 mt-2"><div class="col-md-2"><img src="static/image/akashno.jpg" alt="" class="author-img"></div><div class="col-md-4 blog-details"><p class="author-title m-0 ">@'+item.fields.author_name+'</p><p class="m-0 blog-date text-secondary">'+item.fields.date_created.slice(0,10)+'</p><div class="d-flex m-0 p-0 text-secondary"></div></div></div></div></div><div class="col-md-8 col-12 order-lg-2 order-md-2 order-1"><a href="post/'+item.pk+'" class="text-decoration-none text-reset"><div class="blog-container"><i class="fas fas-envelope" aria-hidden="true"></i><p class="blog-title">'+item.fields.title+'</p><p class="blog-body">'+item.fields.description+'</p><div class="shape-wrapper d-flex"><div class="shape1"></div><div class="shape1"></div><div class="shape1"></div></div></div></a></div></div>');
            /* <div class="d-flex  "><i class="fa fa-comment-o mt-1 mr-1" aria-hidden="true"></i> 31</div>*/
        }
      }
    });
});

