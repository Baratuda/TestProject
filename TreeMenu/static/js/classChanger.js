var activeElementId = sessionStorage.getItem('activate');
$('#'+activeElementId).children('a').css('border','3px solid rgb(20, 104, 150)');

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