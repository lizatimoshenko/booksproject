<html>
  <head>
    % include('head.tpl', title='Люби читать')
  </head>
  <body>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title=book_info['title'])
      <main class="mdl-layout__content mdl-color--grey-100">
        <div class="mld-cell mdl-cell--12-col mdl-card mdl-shadow--2dp ">
          <div class="mdl-grid">
            <div class="mld-cell mdl-cell--6-col">
              <ul class="demo-list-item mdl-list">
                <li class="mdl-list__item">
                  <span class="mdl-list__item-primary-content">
                    Автор:  <a href="/about_author?author={{author}}">
                      {{author}}
                    </a>
                  </span>
                </li>
                <li class="mdl-list__item">
                  <span class="mdl-list__item-primary-content">
                    Первая публикация: {{book_info['published']}}
                  </span>
                </li>
              </li>
              <li class="mdl-list__item">
                <span class="mdl-list__item-primary-content">
                  Аннотация:{{book_info['annotation']}}
                </span>
              </li>
              <li>
                % for g in genres:
                <span class="mdl-chip">
                  <span class="mdl-chip__text">{{g['name']}}</span>
                </span>
                % end
              </li>
            </ul>
            <div class="mdl-card__actions mdl-card--border">
              <input type="hidden" id="t" value="{{book_info['title']}}">
              <button onclick="readFunction()" id="read" type="submit" class=" mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
              Добавить в мои книги
              </button>
              <button onclick="wishFunction()" id="wish" type="submit" class=" mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
              Добавить в мои желания
              </button>
            </div>
          </div>
          <div class="mld-cell mdl-cell--2-col ">
          </div>
          <div class="mld-cell mdl-cell--4-col ">
            <img src="{{book_info['image']}}" width="300" height="400"/>
          </div>
        </div>
      </div>
    </main>
  </div>
  <script src="./static/js/readFunction.js"></script>
  <script src="./static/js/wishFunction.js"></script>
</body>
</html>