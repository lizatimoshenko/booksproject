

<html>
<head>

   <link rel="stylesheet" type="text/css" href="../static/css/styles.css">
    <link rel="stylesheet" type="text/css" href="../static/css/material.min.css">
<link href="https://fonts.googleapis.com/css?family=Roboto:regular,bold,italic,thin,light,bolditalic,black,medium&amp;lang=en" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>

<body>

<div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      <header class="demo-header mdl-layout__header mdl-color--grey-100 mdl-color-text--grey-600">
        <div class="mdl-layout__header-row">
          <h2 class="mdl-layout-title">Settings</h2>
          <div class="mdl-layout-spacer"></div>
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--expandable">
            <label class="mdl-button mdl-js-button mdl-button--icon" for="search">
              <i class="material-icons">search</i>
            </label>
            <div class="mdl-textfield__expandable-holder">
              <input class="mdl-textfield__input" type="text" id="search">
              <label class="mdl-textfield__label" for="search">Enter your query...</label>
            </div>
          </div>
        </div>
      </header>
      <div class="demo-drawer mdl-layout__drawer mdl-color--blue-grey-900 mdl-color-text--blue-grey-50">
        <header class="demo-drawer-header">
          <img src="./static/images/user.png" class="demo-avatar">
          <div class="demo-avatar-dropdown">
            <span>Hello, {{username}}</span>
            <div class="mdl-layout-spacer"></div>
            <button  class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--icon">

              <i class="material-icons" role="presentation">exit_to_app</i>

            </button>

          </div>
        </header>

        <nav class="demo-navigation mdl-navigation mdl-color--blue-grey-800">
          <a class="mdl-navigation__link" href=""><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">home</i>Home</a>
          <a class="mdl-navigation__link" href="/settings"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">star</i>Profile</a>
          <a class="mdl-navigation__link" href=""><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">book</i>Books</a>
          <a class="mdl-navigation__link" href=""><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">list</i>Wishlist</a>
          <a class="mdl-navigation__link" href=""><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">people</i>Following</a>
          <a class="mdl-navigation__link" href=""><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">people</i>Followers</a>
          <a class="mdl-navigation__link" href=""><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">help_outline</i>FAQ</a>

          <div class="mdl-layout-spacer"></div>

        </nav>
           </div>
  <main class="mdl-layout__content mdl-color--grey-100">

<form action="#">
  <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
    <input class="mdl-textfield__input" type="text"" id="sample4" value="{{username}}">
    <label class="mdl-textfield__label" for="sample4">Number...</label>
    <span class="mdl-textfield__error">Input is not a number!</span>
  </div>
</form>
     </main>
</body>



 <a href="/logout"><button>LOGOUT</button></a>


</html>