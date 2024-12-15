document.addEventListener("DOMContentLoaded", () => {
    console.log("404 Page Loaded");

    const linkFancy = document.querySelector(".link-fancy");
    linkFancy.addEventListener("mouseenter", () => {
        linkFancy.style.transition = "color 0.3s ease-in-out";
        linkFancy.style.color = "D9EAFD"; 
    });

    linkFancy.addEventListener("mouseleave", () => {
        linkFancy.style.color = ""; 
    });

    setTimeout(() => {
        window.location.href = "/"; 
    }, 10000); 
    console.error("Page not found. Possible navigation error.");
});
