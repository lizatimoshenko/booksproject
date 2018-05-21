$(document).ready(function () {
    $('.followBtn').click(function () {

        var id = $(this).attr('id');
        console.log(id);
        var fd = new FormData;
        fd.append('user', id);

        $.ajax({
            type: 'POST',
            url: '/follow',
            data: fd,
            contentType: false,
            processData: false,
            success: function (data) {

            },
            error: function (ajaxOptions, thrownError) {

            }
        });


    });
});