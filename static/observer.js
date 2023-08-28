const faders = document.querySelectorAll('.fade-in');
const upSliders = document.querySelectorAll('.slide-up');
const appearOptions= {
        rootMargin: "0px 0px -250px 0px"
};


const appearOnScroll = new IntersectionObserver( function(entries, appearOnScroll){
    entries.forEach(entry => {
        if (!entry.isIntersecting){
            return;
        }

        else{
            entry.target.classList.add('scroll-appear');
            appearOnScroll.unobserve(entry.target);
        }
    })
},appearOptions);


faders.forEach(fader =>{
    appearOnScroll.observe(fader);
});

upSliders.forEach(upSlider =>{
    appearOnScroll.observe(upSlider);
});