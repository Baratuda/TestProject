
$(document).ready(function () {
    //Функция которая в случае нажатия на пункт меню меняет сласс CSS на 
    // has-sub если меню закрывается и has-sub open, если меню открывается 
    $('nav li.has-sub > a').on('click', function () {
      var element = $(this).parent('li');
      if (element.hasClass('open'))
        sessionStorage.setItem(element.attr('id'),'has-sub');
      else 
        sessionStorage.setItem(element.attr('id'),'has-sub open');
      // var x = $('li#'+element.attr('id')+' > ul');
      // var children = $(x);
      // alert(x.length);
      // children.each(function(index) {
      //   alert('#');
      // });
      // for(let i in children){
        
        // var id = i.attr('id');
        // if (i.hasClass('open'))
        //   sessionStorage.setItem(id,'has-sub');
      // }
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

