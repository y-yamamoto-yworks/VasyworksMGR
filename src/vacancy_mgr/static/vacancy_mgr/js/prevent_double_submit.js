document.forms[0].addEventListener('submit', function(e){
    var elements = this.elements;
    for (var n = 0; n < elements.length; n++) {
        if (elements[n].type === 'submit') {
            elements[n].disabled = true;
        }
    }
});
