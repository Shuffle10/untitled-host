// let items = document.querySelectorAll('.header ul li');
// items.forEach(item => {
//     item.addEventListener('click',()=>{
//         document.querySelector('li.active').classList.remove('active');
//         item.classList.add('active');
//     })
// }); 
var rocket = document.getElementById('rocket');

    


window.addEventListener('scroll',function(){
    var header= document.querySelector('nav');
    rocket.classList.remove('fly');
    header.classList.toggle('sticky',window.scrollY>0);
    rocket.style.display = 'inline';
    rocket.classList.toggle('appear', window.scrollY>0);
});

rocket.addEventListener('click',function(){
    rocket.classList.remove('appear');
    rocket.classList.add('fly')
    setTimeout(function(){
        
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
        }, 600);


});



