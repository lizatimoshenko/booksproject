<header class="demo-header mdl-layout__header mdl-color--grey-100 mdl-color-text--grey-600">
  <div class="mdl-layout__header-row">
    <h2 id="title" class="mdl-layout-title">{{title}}</h2>
    <div class="mdl-layout-spacer"></div>
  </div>
</header>
<div class="demo-drawer mdl-layout__drawer mdl-color--blue-grey-900 mdl-color-text--blue-grey-50">
  <header class="demo-drawer-header">
    <img src={{avatar}} class="demo-avatar">
    <div class="demo-avatar-dropdown">
      <span>Hello, {{username}}</span>
      <div class="mdl-layout-spacer"></div>
      <a href="/logout">
      <button  class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--icon">
      <i class="material-icons" role="presentation">exit_to_app</i>
      </button>
      </a>
    </div>
  </header>
 % include('navigation.tpl')
</div>