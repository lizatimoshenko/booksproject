
<html>
<head>
    % include('head.tpl', title='Люби читать')
</head>

<body>

<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title='Список желаний')
       <main class="mdl-layout__content mdl-color--grey-100">
           <div class="mdl-grid">
        % for book in books:
        <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col">
          <form action="" >
            <div class="mdl-grid">
              <img class="mdl-cell mdl-cell--3-col" src="{{book['image']}}" width="150" height="200">

              <div class="mdl-cell mdl-cell--9-col">
                <a href="/read_more?title={{book['title']}}"><p id="username"  class="parag">{{book['title']}}</p></a>
                    <p> {{book['annotation']}}</p>
              </div>
              <div class="mdl-cell mdl-cell--10-offset ">
                <button id="subscribe" type="submit" class="unfollowBtn mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                Читать далее
                </button>
              </div>
            </div>
          </form>
        </div>
        % end
      </div>


       </main>
</div>
</body>

</html>