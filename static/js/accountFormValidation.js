$("#account-information").validate({
    rules: {
        email: {
            required: true,
            email: true
        },
        password: {
            minlength: 5
        },
        confirm: {
            minlength: 5,
            equalTo: "#password"
        }
    },
    messages: {
        email: {
            required: "Введите адрес электронной почты.",
            email: "Введите действительный электронный адрес."
        },
        password: {
            minlength: jQuery.format("Пароль должен содержать не менее {0} символов")
        },
        confirm: {
            minlength: jQuery.format("Пароль должен содержать не менее {0} символов"),
            equalTo: "Пароли не совпадают!"
        }
    },
    errorElement: 'label',
    errorPlacement: function(error, element) {
        toastr.error(error, 'Внимание')
    }
});