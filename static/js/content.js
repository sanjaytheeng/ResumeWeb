// scripts.js

// Smooth scrolling for anchor links (if applicable)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
  
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    });
  });
  
  // Example for adding AOS (Animate On Scroll) animations
  // Ensure AOS library is included in your project
  AOS.init({
    duration: 1200,  // Duration for animations
    easing: 'ease-in-out',  // Easing function
    once: true  // Animation happens only once
  });
  
  // Add or remove class to improve UI/UX
  document.addEventListener('DOMContentLoaded', function() {
    const contentBlock = document.querySelector('.blockquote');
    
    // Example of adding class on scroll
    window.addEventListener('scroll', function() {
      if (window.scrollY > 100) {
        contentBlock.classList.add('scrolled');
      } else {
        contentBlock.classList.remove('scrolled');
      }
    });
  });
  
  // Lazy load images
  document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll("img[data-aos='fade']");
  
    images.forEach(img => {
      img.addEventListener('load', () => {
        img.classList.add('loaded');
      });
    });
  });
  