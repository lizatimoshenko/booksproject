<html>
<head>
    % include('head.tpl', title='Люби читать')
</head>

<body>

<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
    % include('header.tpl', title='Поиск')
    <main class="mdl-layout__content mdl-color--grey-100">

        <div class="mdl-layout__header-row mdl-shadow--2dp mdl-cell mdl-cell--12-col">
            <a href="/following">
                <button class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--colored">
                    Мои подписки
                </button>
            </a>
            <div class="mdl-layout-spacer"></div>
            <div class="mdl-textfield mdl-js-textfield mdl-textfield--expandable mdl-textfield--floating-label mdl-textfield--align-right">
                <label class="mdl-button mdl-js-button mdl-button--icon" for="search">
                    <i class="material-icons">search</i>
                </label>
                <div class="mdl-textfield__expandable-holder">
                    <input class="mdl-textfield__input" type="text" name="sample" id="search"/>
                </div>
            </div>
        </div>

        <div class="mdl-grid">
            % for user in users:
            <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col">

                <form action="">
                    <div class="mdl-grid">

                        <img class="mdl-cell mdl-cell--3-col" id="image" src="{{user['image']}}" width="150" height="150">
                        <div class="mdl-cell mdl-cell--9-col">
                            <a href=""><p id="username" class="parag">{{user['username']}}</p></a>
                            <p class="">Недавно прочитанные</p>
                        </div>


                        <div class="mdl-cell mdl-cell--10-offset ">
                            <button type="submit" id="{{user['username']}}"
                                    class="followBtn mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                                Подписаться
                            </button>
                        </div>
                    </div>
                </form>

            </div>
            % end
        </div>
    </main>
</div>
<script >
    $(document).ready(function() {
     $('.followBtn').click(function () {

         var id = $(this).attr('id');
          console.log(id);
         var fd =new FormData;
		fd.append('user', id);

  $.ajax({
  type: 'POST',
  url: '/follow',
  data: fd,
  contentType: false,
  processData: false,
  success: function(data) {

  console.log(data)
  },
  error: function(ajaxOptions, thrownError) {

  }
  });




     });
 });

</script>
</body>
</html>
