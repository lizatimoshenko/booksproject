/*function follow() {
    var fd = new FormData;

    fd.append('user', $('#username').text());

    $.ajax({
        type: 'POST',
        url: '/follow',
        data: fd,
        contentType: false,
        processData: false,
        success: function(data) {
            toastr.success('Вы подписаны!', {
                timeOut: 5000
            })
            console.log(data)
        },
        error: function(ajaxOptions, thrownError) {
            toastr.error('Возникли ошибки при подключении к серверу.', 'Внимание!')
        }
    });
}*/


