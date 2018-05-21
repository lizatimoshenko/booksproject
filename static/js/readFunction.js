function readFunction() {
    var text = $('#read').text();
    if (text == "Удалить из моих книг") {

        $.ajax({
            type: 'POST',
            url: '/unread_book',

            data: JSON.stringify(
                {'title': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function (res) {

                $('#read').html('Добавить в мои книги');
                console.log(res);
            },
            error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
            }
        });


    } else {

        $.ajax({
            type: 'POST',
            url: '/read_book',

            data: JSON.stringify(
                {'title': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function (res) {

                $('#read').html('Удалить из моих книг');
                console.log(res);
            },
            error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
            }
        });

    }
    ;
}