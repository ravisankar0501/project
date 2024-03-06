document.addEventListener("DOMContentLoaded", function() {
    // Get the about section
    var aboutSection = document.getElementById('about');
    
    // Trigger animation and show about section after some delay (e.g., 2 seconds)
    setTimeout(function() {
        aboutSection.style.animation = 'slideInFromLeft 1s ease-out';
        aboutSection.style.opacity = '1'; // Set opacity to 1 to make the section visible
    }, 2000);

 
});
