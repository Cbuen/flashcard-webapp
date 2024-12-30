// used to flip card
document.querySelector(".flip-card").addEventListener("click", function () {
  this.classList.toggle("flipped");
});

// card-list-button
const card_button = document.getElementById("card-list-button");
const card_items = document.getElementsByClassName("card-item");
const flashcardContainer = document.querySelector(
  ".relative.flex.flex-col.bg-gray-200.rounded-lg.shadow-md"
);

card_button.addEventListener("click", function () {
  for (let i = 0; i < card_items.length; i++) {
    if (card_items[i].classList.contains("hidden")) {
      card_items[i].classList.remove("hidden");
      allHidden = false;
    } else {
      card_items[i].classList.add("hidden");
      allHidden = true;
    }
  }

  // Resize flashcard container
  if (allHidden) {
    flashcardContainer.classList.add("h-24"); // Shrink container
    flashcardContainer.classList.remove("h-auto");
  } else {
    flashcardContainer.classList.remove("h-24"); // Expand container
    flashcardContainer.classList.add("h-auto");
  }
});

// card-set-button
const card_buttons = document.getElementsByClassName("card-set-button");
const language_header = document.getElementById("lang-header");

// Add click event listener to each card-set-button
for (let i = 0; i < card_buttons.length; i++) {
  card_buttons[i].addEventListener("click", function () {
    // Update the language header with the clicked button's text
    language_header.textContent = this.textContent;
  });
}
