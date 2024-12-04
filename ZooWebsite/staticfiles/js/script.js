document.querySelectorAll('.dropdown').forEach((dropdown) => {
    dropdown.addEventListener('mouseover', () => {
        const menu = dropdown.querySelector('.dropdown-menu');
        if (menu) menu.style.display = 'block';
    });
    dropdown.addEventListener('mouseout', () => {
        const menu = dropdown.querySelector('.dropdown-menu');
        if (menu) menu.style.display = 'none';
    });
});

window.addEventListener('scroll', function() {
    var footer = document.querySelector('.footer');
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        footer.style.bottom = '0';
    } else {
        footer.style.bottom = '-100px';
    }
});