console.log("JS carregado!"); // This one is working

document.addEventListener("DOMContentLoaded", function () {
    console.log("DOMContentLoaded fired!"); // Add this
    const reveals = document.querySelectorAll(".reveal");
    console.log("Found " + reveals.length + " reveal elements."); // Add this

    // If reveals.length is 0, then querySelectorAll isn't finding anything.
    // This would be a major clue.

    const observer = new IntersectionObserver((entries) => {
        console.log("IntersectionObserver callback fired!"); // Add this
        entries.forEach((entry) => {
            console.log("Entry is intersecting: " + entry.isIntersecting + ", target: ", entry.target); // Add this
            if (entry.isIntersecting) {
                console.log("Adding 'visible' class to: ", entry.target); // Add this
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    reveals.forEach((section) => {
        console.log("Observing section: ", section.id); // Add this
        observer.observe(section);
    });
});

