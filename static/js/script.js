// FIXME: animation resets on page update

let pos = localStorage.getItem('bgPos') || 0;
let startTime = localStorage.getItem('startTime') || Date.now();
const duration = 15000; // 15 seconds in milliseconds

function easeInOut(t) {
    // Recreates the 'ease' timing function
    return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
}

function animateBackground() {
    // Store startTime if it's new
    if (!localStorage.getItem('startTime')) {
        localStorage.setItem('startTime', startTime);
    }
    
    const elapsed = (Date.now() - startTime) % duration;
    const progress = elapsed / duration;
    
    // Calculate position using the ease function (0 to 100)
    pos = easeInOut(progress) * 100;
    
    document.body.style.backgroundPosition = `${pos}% 50%`;
    localStorage.setItem('bgPos', pos);
    requestAnimationFrame(animateBackground);
}

animateBackground();