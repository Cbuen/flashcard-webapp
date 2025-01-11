function deleteCardHelper(button) {
  console.log("delete card");
  document
    .getElementById("hidden-card-id")
    .setAttribute("value", button.getAttribute("data-cardid"));
}
