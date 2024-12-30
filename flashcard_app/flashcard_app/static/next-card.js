document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelectorAll(".flip-card");
  let currentCardIndex = 0;

  const prev_button = document.getElementById("prev-btn");
  prev_button.addEventListener("click", function () {
    showCard(currentCardIndex - 1);
  });

  const next_button = document.getElementById("next-btn");
  next_button.addEventListener("click", function () {
    showCard(currentCardIndex + 1);
  });

  function showCard(index) {
    if (index < 0) index = cards.length - 1;
    if (index >= cards.length) index = 0;

    cards[currentCardIndex].classList.add("hidden");
    cards[index].classList.remove("hidden");
    currentCardIndex = index;
  }

  cards.forEach((card) => {
    card.addEventListener("click", function () {
      this.classList.toggle("flipped");
    });
  });
});
