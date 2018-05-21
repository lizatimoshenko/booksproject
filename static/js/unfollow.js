$(document).ready(function () {
    $('.unfollowBtn').click(function () {

        var id = $(this).attr('id');
        console.log(id);
        var fd = new FormData;
        fd.append('user', id);
        $.ajax({
            type: 'POST',
            url: '/unfollow',
            data: fd,
            contentType: false,
            processData: false,
            success: function (data) {

                console.log(data)
            },
            error: function (ajaxOptions, thrownError) {

            }
        });


    });
});