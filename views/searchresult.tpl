<html>
  <head>
    % include('head.tpl', title='Поиск')
  </head>
  <body>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('searchHeader.tpl', title='Поиск')
    <main class="mdl-layout__content mdl-color--grey-100">
      <div class="mdl-grid">
        % for user in users:
        <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col">
          <form action="">
            <div class="mdl-grid">
              <img class="mdl-cell mdl-cell--3-col" id="image" src="{{user['image']}}" width="150" height="150">
              <div class="mdl-cell mdl-cell--9-col">
                % if user['username']==username:
                <a href=""><p id="username" class="parag">Я</p></a>
                % else:
                <a href=""><p id="username" class="parag">{{user['username']}}</p></a>
                % end
                <p class="">Недавно прочитанные</p>
                <ul class="demo-list-item mdl-list">
                   % for book in user_books[user['username']]:
                <li class="mdl-list__item">
                  <span class="mdl-list__item-primary-content">
                    <a href="/read_more?title={{book['title']}}">
                      {{ dict(book)['title'] }}
                    </a>
                  </span>
                </li>
                  % end
                </ul>
              </div>
              <div class="mdl-cell mdl-cell--10-offset ">
                % if (user['username'] in followings) and (user['username']!=username):
                <button type="submit" id="{{user['username']}}"
                class="unfollowBtn mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                Отписаться
                </button>
                % end
                % if (user['username'] not in followings) and (user['username']!=username):
                <button type="submit" id="{{user['username']}}"
                class="followBtn mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                Подписаться
                </button>
                % end
              </div>
            </div>
          </form>
        </div>
        % end
      </div>
    </main>
  </div>
  <script src="./static/js/follow.js"></script>
  <script src="./static/js/unfollow.js"></script>
</body>
</html>