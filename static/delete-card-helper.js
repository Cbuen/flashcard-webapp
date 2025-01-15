function deleteCardHelper(element) {
  const cardId = element.getAttribute("data-cardid");
  document.getElementById("hidden-card-id").value = cardId;
}
