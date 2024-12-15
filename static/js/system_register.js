document.addEventListener("DOMContentLoaded", () => {
    console.log("Register Page Loaded");

    const emailInput = document.getElementById("exampleInputEmail1");
    const passwordInput = document.getElementById("exampleInputPassword1");
    const form = document.querySelector("form");
    const newsletterCheck = document.getElementById("exampleCheck1");

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (!validateEmail(email)) {
            alert("Please enter a valid email address.");
            return;
        }

        if (password.length < 8) {
            alert("Password must be at least 8 characters long.");
            return;
        }

        console.log("Form submitted successfully:", { email, password });
        alert("Account created successfully! Check your email for confirmation.");

        window.location.href = "/dashboard";
    });

    [emailInput, passwordInput].forEach((input) => {
        input.addEventListener("focus", () => {
            input.classList.add("is-focused");
        });
        input.addEventListener("blur", () => {
            input.classList.remove("is-focused");
        });
    });

    newsletterCheck.addEventListener("change", () => {
        if (newsletterCheck.checked) {
            console.log("User opted out of the newsletter.");
        } else {
            console.log("User agreed to receive the newsletter.");
        }
    });

    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }
});