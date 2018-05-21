<html>
  <head>
    % include('head.tpl', title='Мои писатели')
  </head>
  <body>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      <header class="demo-header mdl-layout__header mdl-color--grey-100 mdl-color-text--grey-600">
        <div class="mdl-layout__header-row">
          <h2 id="title" class="mdl-layout-title">Мои писатели</h2>
          <div class="mdl-layout-spacer"></div>
          <form action="/search_authors" method="POST">
            <div class="mdl-textfield mdl-js-textfield mdl-textfield--expandable mdl-textfield--floating-label mdl-textfield--align-right">
              <label class="mdl-button mdl-js-button mdl-button--icon" for="search">
                <i class="material-icons">search</i>
              </label>
              <div class="mdl-textfield__expandable-holder">
                <input class="mdl-textfield__input" type="text" name="search" id="search"/>
              </div>
            </div>
            <button id="searchBtn" type="submit"
            class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--colored">
            Поиск
            </button>
          </form>
        </div>
      </header>
      <div class="demo-drawer mdl-layout__drawer mdl-color--blue-grey-900 mdl-color-text--blue-grey-50">
        <header class="demo-drawer-header">
          <img src={{avatar}} class="demo-avatar">
          <div class="demo-avatar-dropdown">
            <span>Hello, {{username}}</span>
            <div class="mdl-layout-spacer"></div>
            <a href="/logout">
              <button class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--icon">
              <i class="material-icons" role="presentation">exit_to_app</i>
              </button>
            </a>
          </div>
        </header>
        % include('navigation.tpl')
      </div>
    <main class="mdl-layout__content mdl-color--grey-100">
      <div class="mdl-grid">
        % for author in authors:
        <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col">
          <form action="" >
            <div class="mdl-grid">
              <img class="mdl-cell mdl-cell--3-col" src="{{author['image']}}" width="100" height="150">
              <div class="mdl-cell mdl-cell--9-col">
                <a href="/about_author?author={{author['name']}}"><p id="username"  class="parag">{{author['name']}}</p></a>
                <p class="">Книги</p>
                <ul class="demo-list-item mdl-list">
                   % for book in user_books[author['name']]:
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
                <button id="subscribe" type="submit" class="unfollowBtn mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                Отписаться
                </button>
              </div>
            </div>
          </form>
        </div>
        % end
      </div>
    </main>
    </div>
  <script src="./static/js/myFunction.js"></script>
</body>
</html>