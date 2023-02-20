const form = document.querySelector('.input-expand6');

form.addEventListener('mouseover',() => {
    var myForm = form.clientWidth;
    form.style.width = (myForm + 150) + "px";
});

form.addEventListener('mouseout',() => {
    var myForm = form.clientWidth;
    form.style.width = (myForm - 142) + "px";
});
