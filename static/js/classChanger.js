// При загрузке страницы меняет стиль активного элемента
var activeElementId = sessionStorage.getItem('activate');
$('#'+activeElementId).children('a').css('border','3px solid rgb(20, 104, 150)');
// Регулирует отступы меню 
$('ul').each(function(index) {
    var len = $(this).parents('ul').length;
    var padding = 20+len*15 + 'px';
    $(this).children('li').children('a').css('padding-left',padding);
});
// При загрузке страницы меняет все сохраненные классы в sessionStorage
// и в зависимости от полученого класса закрывают или раскрывают меню или подменю 
for(let key in sessionStorage) {
    if (!sessionStorage.hasOwnProperty(key)) 
        continue; 
    var element = $('#'+key);
    element.attr('class', sessionStorage.getItem(key));
    if(element.attr('class').includes('has-sub open'))
        element.children('ul').show();
    else
        element.children('ul').hide();
  
}  