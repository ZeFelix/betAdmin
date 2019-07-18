function deleteSignPlan(message, parent) {
    message = 'Deseja apagar Plano código ' + message
    if (confirm(message)) {
        parent.parentNode.submit()
    }
}