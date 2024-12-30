document.addEventListener('DOMContentLoaded', () => {
    const carouselContainer = document.getElementById('carousel-container');

    // Listen for wheel events to implement horizontal scrolling with the touchpad
    carouselContainer.addEventListener('wheel', (event) => {
        if (event.deltaY !== 0) {
            event.preventDefault();
            carouselContainer.scrollBy({
                left: event.deltaY,
                behavior: 'smooth'
            });
        }
    });
});
