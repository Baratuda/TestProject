
$(document).ready(function () {
    //Функция которая в случае нажатия на пункт меню меняет сласс CSS на 
    // has-sub если меню закрывается и has-sub open, если меню открывается 
    $('nav li.has-sub > a').on('click', function () {
      var element = $(this).parent('li');
      var id = element.attr('id');
      if (element.hasClass('open'))
        sessionStorage.setItem(id,'has-sub');
      else 
        sessionStorage.setItem(id,'has-sub open');
      // Код сварачивает все дочерние подменю если основное меню свернуто
      element.find('*').each(function(index) {
         if($(this).attr('class')=='has-sub open')
            sessionStorage.setItem($(this).attr('id'),'has-sub');
      });
    });
  
    //Функция которая в случае нажатия на пункт меню делает его активным
    $('a').on('click', function () {
      var element = $(this).parent('li');
      var id = element.attr('id');
      sessionStorage.setItem('activate', id);
    }); 

    //Стилизация тега nav>ul>li.has-sub>a
    $('nav>ul>li.has-sub>a').append('<span class="holder"></span>');
});

