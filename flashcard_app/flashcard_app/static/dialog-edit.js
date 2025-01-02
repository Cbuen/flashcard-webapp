function buttonTest(button) {
  const term = button.getAttribute('data-term');
  const definition = button.getAttribute('data-definition');

  console.log(button.id);
  console.log(term);
  console.log(definition);
}

function clearInput() {
  document.querySelectorAll("input.clear-input").forEach(input => input.value = '');

}
