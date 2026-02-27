// Mobile nav toggle
document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.querySelector(".nav-toggle");
    const nav = document.getElementById("site-nav");

    if (toggle && nav) {
        toggle.addEventListener("click", function () {
            nav.classList.toggle("open");
            const expanded = toggle.getAttribute("aria-expanded") === "true";
            toggle.setAttribute("aria-expanded", !expanded);
        });
    }
});

// Close mobile nav on HTMX navigation
document.addEventListener("htmx:beforeRequest", function () {
    const nav = document.getElementById("site-nav");
    if (nav) nav.classList.remove("open");
});
