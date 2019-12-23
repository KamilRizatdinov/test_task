let query_form = document.getElementById('query');
let query_type = document.getElementById('query-type');
query_form.addEventListener('input', UpdateListener);

function UpdateListener(input) {
    let length = input.target.value.length;
    if (length === 13) {
        query_type.innerText = "OGRN";
    } else if (length === 10) {
        query_type.innerText = "INN";
    } else {
        query_type.innerText = "Unkown";
    }
}
