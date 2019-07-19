function deleteSignPlan(message, parent) {
    message = 'Deseja apagar Plano código ' + message
    if (confirm(message)) {
        parent.parentNode.submit()
    }
}

function changeAccountPayment(parent) {
    var jqxhr = $.get("/payments/administrator-account/" + parent.value, function(data) {
            fill(data)
        })
        .fail(function() {
            location.reload();
        });
}

function fill(params) {
    Object.entries(params).forEach(([key, value]) => {
        $('#' + key).text(value);
    });
}