document.querySelector(".flip-card").addEventListener("click", function () {
  this.classList.toggle("flipped");
});

// test code
let w1 = "hola";
let w2 = "nombre";
let w3 = "como estas";
const words = [w1, w2, w3];

// card-list-button
const card_button = document.getElementById("card-list-button");
const card_items = document.getElementsByClassName("card-item");

card_button.addEventListener("click", function () {
  for (let i = 0; i < card_items.length; i++) {
    if (card_items[i].classList.contains("hidden")) {
      card_items[i].classList.remove("hidden");
    } else {
      card_items[i].classList.add("hidden");
    }
  }
});
