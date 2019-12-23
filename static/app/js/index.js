let query_form = document.getElementById('query');
let query_type = document.getElementById('query-type');
let submit_button = document.getElementById('submit-btn');
query_form.addEventListener('input', UpdateListener);

function UpdateListener(input) {
    let length = input.target.value.length;
    if (length === 13) {
        query_type.innerText = "OGRN";
        submit_button.disabled = false;
    } else if (length === 10) {
        query_type.innerText = "INN";
        submit_button.disabled = false;
    } else {
        query_type.innerText = "Unkown";
        submit_button.disabled = true;
    }
}
