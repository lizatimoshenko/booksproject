
<html>
<head>
    % include('head.tpl', title='Люби читать')
</head>

<body>

<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title='Поиск')
  <main class="mdl-layout__content mdl-color--grey-100">
   <div class="mdl-grid">
     % for name in usernames:
     <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col">
      <form action="/follow/{{name}}">
        <h4 class="">{{name}}</h4>
         <!--add recent read-->

     <button type="submit" class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect">
        <i class="material-icons">add</i>
     </button>

     </div>

       % end
   </div>
 </main>
</body>

</html>