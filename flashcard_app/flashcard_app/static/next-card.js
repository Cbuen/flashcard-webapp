document.addEventListener("DOMContentLoaded", function () {
  const prev_button = document.getElementById("prev-btn");
  prev_button.addEventListener("click", function () {
    console.log("Prev Button Clicked");
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const next_button = document.getElementById("next-btn");
  next_button.addEventListener("click", function () {
    console.log("Next Button Clicked");
  });
});
