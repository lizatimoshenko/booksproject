function myFunction() {
    var text = $('#subscribe').text();
    if (text == "Отписаться") {
        $.ajax({
            type: 'POST',
            url: '/unsubscribe_author',
            data: JSON.stringify(
                {'name': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function (res) {
                $('#subscribe').html('Подписаться');
                console.log(res);
            },
            error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
            }
        });
    } else {
        $.ajax({
            type: 'POST',
            url: '/subscribe_author',
            data: JSON.stringify(
                {'name': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function (res) {
                $('#subscribe').html('Отписаться');
                console.log(res);
            },
            error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
            }
        });
    }
    ;
}