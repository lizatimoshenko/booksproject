function wishFunction() {
    var text = $('#wish').text();
    if (text == "Удалить из желаний") {

        $.ajax({
            type: 'POST',
            url: '/delete_wish',

            data: JSON.stringify(
                {'title': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function (res) {

                $('#wish').html('Добавить в мои желания');
                console.log(res);
            },
            error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
            }
        });


    } else {

        $.ajax({
            type: 'POST',
            url: '/add_wish',

            data: JSON.stringify(
                {'title': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function (res) {

                $('#wish').html('Удалить из желаний');
                console.log(res);
            },
            error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
            }
        });

    }
    ;
}