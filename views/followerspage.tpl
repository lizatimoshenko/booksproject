
<html>
<head>
    % include('head.tpl', title='Люби читать')
</head>

<body>

<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title='Подписчики')
  <main>
   <div class="mdl-grid">
     % for name in usernames:
     <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col">
      <form action="/follow/{{name}}">
        <h4 class="">{{name}}</h4>
         <!--add recent read-->
     </div>

       % end
   </div>
  </main>
</div>
</body>

</html>