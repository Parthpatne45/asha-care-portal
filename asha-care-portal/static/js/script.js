// ===== Mobile Navbar Toggle =====
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Auto-hide flash messages after 5 seconds
document.querySelectorAll('.flash-message').forEach(flash => {
    setTimeout(() => {
        flash.style.opacity = '0';
        flash.style.transition = 'opacity 0.5s';
        setTimeout(() => flash.remove(), 500);
    }, 5000);
});
