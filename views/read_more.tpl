<html>
  <head>
    % include('head.tpl', title=title)
  </head>
  <body>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title=title)
      <main>
        <div class="mdl-grid">
          <div class="mdl-cell mdl-cell--6-col">
            <ul class="demo-list-item mdl-list">
              <li class="mdl-list__item">
                <span class="mdl-list__item-primary-content">
                  Author:
                </span>
              </li>
              <li class="mdl-list__item">
                <span class="mdl-list__item-primary-content">
                  Published: {{published}}
                </span>
              </li>
              <li class="mdl-list__item">
                <span class="mdl-list__item-primary-content">
                  Language: {{language}}
                </span>
              </li>
              <li class="mdl-list__item">
                <span class="mdl-list__item-primary-content">
                  Annotation : {{annotation}}
                </span>
              </li>
            </ul>
          </div>
          <div class="mdl-cell mdl-cell--6-col">
            <img src={{image}}>
          </div>
        </div>
      </main>
    </div>
  </body>
</html>