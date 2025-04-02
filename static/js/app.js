document.addEventListener('click', function(e) {
    if (e.target.classList.contains('spoiler')) {
        e.target.classList.add('revealed');
    }
});