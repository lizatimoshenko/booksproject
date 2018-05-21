<html>
<head>
    % include('head.tpl', title='Настройки профиля')
</head>
<body>
<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
    % include('header.tpl', title='Настройки профиля')
    <main class="mdl-layout__content mdl-color--grey-100">
        <div class="mdl-grid">
            <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--6-col">
                % include('account_settings.tpl')
            </div>
            <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--6-col">
                % include('personal_settings.tpl')
            </div>


            <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col mdl-cell--middle">
                % include('preferences.tpl')
            </div>
        </div>
    </main>

</div>
<script>
    document.getElementById("upload").onchange = function () {
        document.getElementById("uploadFile").value = this.files[0].name;
        if ($("#uploadFile").val() != "") {
            $("#uploadFile").focus()
        }

    };

</script>
<script src="./static/js/addPreferences.js"></script>
<script src="./static/js/changePersonalData.js"></script>
<script src="./static/js/changeAccountInfo.js"></script>
<script src="./static/js/accountFormValidation.js"></script>
</body>
</html>