const edit_container = document.getElementById("edit-container");

function hideContainer() {
  edit_container.classList.add("hidden");
  document.getElementById("set-input").setAttribute("value", 0);
}

function showContainer() {
  edit_container.classList.remove("hidden");
}
