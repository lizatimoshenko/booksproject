<html>
<head>
    % include('head.tpl', title='Люби читать')
</head>

<body>

<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
    % include('header.tpl', title='Рекомендации')
    <main class="mdl-layout__content mdl-color--grey-100">

        <div class="mdl-grid">

 <!--Last added books-->
            <h4 class="mdl-card__title-text">Недавно добавленные</h4>
            <div class="mdl-grid mdl-cell mdl-cell--12-col mdl-card mdl-shadow--2dp">
                % for book in last_added_books:

                    <div class="mdl-cell mdl-cell--3-col mdl-card mdl-shadow--2dp">


                        <div class="mdl-card__title">
                            <h4 class="mdl-card__title-text">{{book['title'][:13]}}</h4>
                        </div>
                        <div class="mdl-card__supporting-text">
                            {{book['annotation'][:100]}}...
                        </div>
                        <div class="mdl-card__actions mdl-card--border">
                            <a href="/read_more?title={{book['title']}}">
                            <button type="submit" class=" mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                                Читать далее
                                </button>
</a>
                        </div>

                </div>

                  % end
            </div>

             <!--By followers-->
            <h4 class="mdl-card__title-text">Ваши подписки читают </h4>
            <div class="mdl-grid mdl-cell mdl-cell--12-col mdl-card mdl-shadow--2dp">
                % for book in user_books:

                    <div class="mdl-cell mdl-cell--3-col mdl-card mdl-shadow--2dp">


                        <div class="mdl-card__title">
                            <h4 class="mdl-card__title-text">{{book['title'][:13]}}</h4>
                        </div>
                        <div class="mdl-card__supporting-text">
                            {{book['annotation'][:100]}}...
                        </div>
                        <div class="mdl-card__actions mdl-card--border">
                            <a href="/read_more?title={{book['title']}}">
                            <button type="submit" class=" mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                                Читать далее
                                </button>
</a>
                        </div>

                </div>

                  % end
            </div>

             <!--By followings-->
            <h4 class="mdl-card__title-text">Ваши подписчики читают</h4>
            <div class="mdl-grid mdl-cell mdl-cell--12-col mdl-card mdl-shadow--2dp">
                % for book in user_books1:

                    <div class="mdl-cell mdl-cell--3-col mdl-card mdl-shadow--2dp">


                        <div class="mdl-card__title">
                            <h4 class="mdl-card__title-text">{{book['title'][:13]}}</h4>
                        </div>
                        <div class="mdl-card__supporting-text">
                            {{book['annotation'][:100]}}...
                        </div>
                        <div class="mdl-card__actions mdl-card--border">
                            <a href="/read_more?title={{book['title']}}">
                            <button type="submit" class=" mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                                Читать далее
                                </button>
</a>
                        </div>

                </div>

                  % end
            </div>



        </div>

</main>
</div>


</body>

</html>