function changeAccountInfo() {
    var fd = new FormData;

    fd.append('email', $('#email').val());
    fd.append('password', $('#password').val());
    fd.append('confirm', $('#confirm').val());
    $.ajax({
        type: 'POST',
        url: '/change_account_info',
        data: fd,
        contentType: false,
        processData: false,
        success: function(data) {
            toastr.success('Изменения прошли успешно', {
                timeOut: 5000
            })
            console.log(data)
        },
        error: function(ajaxOptions, thrownError) {
            toastr.error('Возникли ошибки при подключении к серверу.', 'Внимание!')
        }
    });
}