<html>
  <head>
    % include('head.tpl', title=name)
  </head>
  <body>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title=name)
      <main class="mdl-layout__content mdl-color--grey-100">
        <div class="mld-cell mdl-cell--12-col mdl-card mdl-shadow--2dp ">
          <div class="mdl-grid">
            <div class="mdl-cell mdl-cell--5-col">
              <div class="mdl-card__actions mdl-card--border"></div>
              <h4>Книги автора</h4>
              % for book in books:
              <div class="mdl-cell mdl-cell--9-col mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title">
                  <a href="/read_more?title={{book['title']}}"><h4 class="mdl-card__title-text">{{book['title']}}</h4></a>
                </div>
                <img src="{{book['image']}}">
              </div>
              % end
              <button onclick="myFunction()"  id="subscribe" class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">Подписаться
              </button>
            </div>
            <div class="mld-cell mdl-cell--1-col ">
            <div class="mld-cell mdl-cell--5-col ">
              <img src={{image}}  width="300" height="400">
            </div>
          </div>
        </div>
        </div>
      </main>
    </div>
    <script src="./static/js/myFunction.js"></script>
  </body>
</html>