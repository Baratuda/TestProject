
$(document).ready(function () {
    $('nav li.has-sub > a').on('click', function () {
      var element = $(this).parent('li');
      if (element.hasClass('open'))
        sessionStorage.setItem(element.attr('id'),'has-sub');
      else 
        sessionStorage.setItem(element.attr('id'),'has-sub open');
    });

    $('a').on('click', function () {
      var element = $(this).parent('li');
      var id = element.attr('id');
      sessionStorage.setItem('activate', id);
    });   
    
    $('nav>ul>li.has-sub>a').append('<span class="holder"></span>');
});

