function changePersonalData() {
    var $input = $("#upload");
    var fd = new FormData;
    fd.append('file', $input.prop('files')[0]);
    fd.append('name', $("#name").val());
    fd.append('surname', $("#surname").val());
    $.ajax({
        type: 'POST',
        url: '/change_personal_information',
        data: fd,
        contentType: false,
        processData: false,
        success: function(data) {
            toastr.success('Изменения прошли успешно!', {
                timeOut: 5000
            })
            console.log(data)
        },
        error: function(ajaxOptions, thrownError) {
            toastr.error('Возникли ошибки подключения к серверу.', 'Внимание!')
        }
    });
}