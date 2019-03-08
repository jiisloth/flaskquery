
$(document).ready(function () {
    $('input[type=radio][name=alcohol]').change(function() {
        if (document.getElementById('alcohol-0').checked) {
            $('#drinks').show()
        } else {
            $('#drinks').hide()
        }
    });
    $('input[type=checkbox][name=attend]').change(function() {
        if (document.getElementById('attend').checked) {
            $('#attend_box').show();
            $('#avec_consent').prop("checked", false);
        } else {
            $('#attend_box').hide();
            $('#avec_consent').prop("checked", true);
        }
    });
});