let query_form = document.getElementById('query');
let query_type = document.getElementById('query-type');
let submit_button = document.getElementById('submit-btn');
let reg = /^\d+$/;

query_form.addEventListener('input', UpdateListener);

function UpdateListener(input) {
    let query = input.target.value;
    let length = query.length;
    if ((length === 13) && reg.exec(query)) {
        query_type.innerText = "OGRN";
        submit_button.disabled = false;
    } else if ((length === 10) && reg.exec(query)) {
        query_type.innerText = "INN";
        submit_button.disabled = false;
    } else {
        query_type.innerText = "Unkown";
        submit_button.disabled = true;
    }
}
