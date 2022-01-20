

document.getElementById('search-btn').addEventListener('click',function(){
        var search  = document.getElementById('search-bar').value;

        
        
        
        var html = ' <div class="row"> <div class="col span-1-of-3 style"> <img src="{{collect.img.url}}" alt="the song image"> <p> SONG NAME : {{collect.name}} </p>  </div> </div>';

        newHtml = html.replace('{{collect.img.url}}', 'static/images/' + search + '.jpg');

        newHtml = newHtml.replace('{{collect.name}}', search);

        document.querySelector('.section-search').insertAdjacentHTML('beforeend',newHtml);
});



