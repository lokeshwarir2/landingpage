document.addEventListener("DOMContentLoaded", function () {
  const userNumberElement = document.getElementById("userNumber");
  const v=document.getElementById("userNumber").innerText;
    const targetValue = parseInt(v); 
  const incrementInterval = 100; // Speed of incrementing in milliseconds
  let currentValue = 0;

  const increaseCounter = () => {
    if (currentValue < targetValue) {
      currentValue++; // Increase the current value
      userNumberElement.textContent = currentValue; // Update the displayed number
      userNumberElement.classList.add("animated"); // Apply the animation
    }
  };

  // Set the interval to increment the counter every 100 milliseconds
  setInterval(increaseCounter, incrementInterval);
});

// For the transfromation
document.addEventListener("DOMContentLoaded", function () {
  // Get the sections to reveal
  const userNumberSection = document.getElementById("userNumber");
  const messageSection = document.getElementById("message");

  // Add a delay to simulate the page loading and then reveal the content
  setTimeout(() => {
    userNumberSection.classList.add("reveal");
    messageSection.classList.add("reveal");
  }, 500); // Delay to ensure the transition effect is visible
});

const scrollRevealOption = {
  distance: "50px",
  origin: "bottom",
  duration: 1000,
};

ScrollReveal().reveal(".header__container .section__subheader", {
  ...scrollRevealOption,
});
ScrollReveal().reveal(".header__container .section__header", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".header__container .scroll__btn", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".header__container .header__socials", {
  ...scrollRevealOption,
  origin: "left",
  delay: 1500,
});

ScrollReveal().reveal(".about__image-1, .about__image-3", {
  ...scrollRevealOption,
  origin: "right",
});
ScrollReveal().reveal(".about__image-2", {
  ...scrollRevealOption,
  origin: "left",
});
ScrollReveal().reveal(".about__content .section__subheader", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".about__content .section__header", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".about__content p", {
  ...scrollRevealOption,
  delay: 1500,
});
ScrollReveal().reveal(".about__content .about__btn", {
  ...scrollRevealOption,
  delay: 2000,
});
