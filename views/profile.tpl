
<html>
<head>
    % include('head.tpl', title='Люби читать')
</head>

<body>

<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title='Рекомендации')
       <main class="mdl-layout__content mdl-color--grey-100">
         <div class="mdl-grid">
            <div class="demo-card-square mdl-card mdl-shadow--2dp">
  <div class="mdl-card__title mdl-card--expand">
    <img src="{{image}}">
    <h2 class="mdl-card__title-text">{{title}}</h2>
  </div>
  <div class="mdl-card__actions mdl-card--border">
    <a href="/read_more/{{title}}" class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
      Читать
    </a>
  </div>
</div>
         </div>
       </main>
</div>
</body>

</html>