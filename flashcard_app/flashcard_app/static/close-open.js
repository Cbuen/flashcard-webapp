const edit_container = document.getElementById("edit-container");
const term_container = document.getElementById("term-container");

function hideContainer() {
  edit_container.classList.add("hidden");
  term_container.classList.add("hidden");
  document.getElementById("set-input").setAttribute("value", 0);
}

function showContainer() {
  edit_container.classList.remove("hidden");
  // Keep term container hidden initially when showing edit container
  term_container.classList.add("hidden");
}

// Add this new function specifically for the term container
function hideTermContainer() {
  term_container.classList.add("hidden");
}
