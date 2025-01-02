function userSet(button) {
  const term = button.getAttribute('data-term');
  const definition = button.getAttribute('data-definition');
  const selected_set = button.getAttribute('data-selectedset');
  const input_fields = document.querySelectorAll("input.clear-input");

  input_fields[0].value = term;
  input_fields[0].id = button.id;
  input_fields[1].value = definition;
  input_fields[2].value = selected_set;
}

function clearInput() {
  document.querySelectorAll("input.clear-input").forEach(input => input.value = '');

}