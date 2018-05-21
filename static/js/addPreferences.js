function addPreferences() {
    var fd = new FormData;
    var preferences = [];
    $('input:checked').map(function () {
        preferences.push($(this).val());
    })


    fd.append('preferences', preferences);

    $.ajax({
        type: 'POST',
        url: '/add_preferences',
        data: fd,
        contentType: false,
        processData: false,
        success: function (data) {
            toastr.success('Изменения прошли успешно', {
                timeOut: 5000
            })
            console.log(data)
        },
        error: function (ajaxOptions, thrownError) {
            toastr.error('Возникли ошибки при подключении к серверу.', 'Внимание!')
        }
    })
}