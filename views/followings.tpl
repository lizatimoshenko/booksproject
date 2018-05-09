
<html>
<head>
    % include('head.tpl', title='Подписки')
</head>

<body>

<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title='Подписки')
   <main class="mdl-layout__content mdl-color--grey-100">
      <div class="mdl-grid">
         <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--6-col">
         <div class="mdl-grid">
            <h4 class="">Мои подписчики</h4>
             <a href="/searchpeople">
            <button class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--colored">
             <i class="material-icons">add</i>
            </button>
            </a>
         </div>
         </div>
         <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--6-col">
         <div class="mdl-grid">
            <h4 class="">Мои авторы</h4>
            <a href="/searchpeople">
            <button class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--colored">
             <i class="material-icons">add</i>
            </button>
            </a>
         </div>
         </div>
      </div>
     </main>
</div>
</body>

</html>