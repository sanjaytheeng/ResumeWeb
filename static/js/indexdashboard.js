// Smooth Scroll for Anchors
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
  
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth',
        block: 'start',
      });
    });
  });
  
  // Adding a Scroll to Top button (if you want to include a button to scroll back to the top)
  const scrollTopButton = document.createElement('button');
  scrollTopButton.innerHTML = '↑';
  scrollTopButton.classList.add('scroll-to-top');
  document.body.appendChild(scrollTopButton);
  
  scrollTopButton.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
  
  // Scroll to Top Button Visibility Based on Scroll Position
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      scrollTopButton.style.display = 'block';
    } else {
      scrollTopButton.style.display = 'none';
    }
  });
  
  // Example of using CSS classes for animation
  document.addEventListener('DOMContentLoaded', () => {
    const elementsToAnimate = document.querySelectorAll('.animate-on-load');
  
    elementsToAnimate.forEach(element => {
      element.classList.add('fade-in');
    });
  });
  