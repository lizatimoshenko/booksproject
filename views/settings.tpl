<html>
<head>
  % include('head.tpl', title='Настройки профиля')
</head>
  <body>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title='Настройки профиля')
      <main class="mdl-layout__content mdl-color--grey-100">
        <div class="mdl-grid" align="center">
          <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--6-col">
            <h4>Account information</h4>
            <form>
              <div class="mdl-cell mdl-cell--10-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label ">
                <input class="mdl-textfield__input" type="text" id="username" name="username" value="{{username}}" disabled>
                <label class="mdl-textfield__label" for="username">Username</label>
              </div>
              <div class="mdl-cell mdl-cell--10-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                <input class="mdl-textfield__input" type="email" id="email" name="email" value="{{email}}">
                <label class="mdl-textfield__label" for="email">Email</label>
              </div>
              <div class="mdl-cell mdl-cell--12-col">
                <div class=" mdl-cell mdl-cell--5-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                  <input class="mdl-textfield__input" type="password" id="password" name="password" value="">
                  <label class="mdl-textfield__label" for="password">New Password</label>
                </div>
                <div class=" mdl-cell mdl-cell--5-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                  <input class="mdl-textfield__input" type="password" id="confirm" name="confirm" value="">
                  <label class="mdl-textfield__label" for="confirm">Confirm a new password</label>
                </div>
              </div>
              <div class="mdl-cell">
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                Button
                </button>
              </div>
            </form>
          </div>
          <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--6-col">
            <h4>Personal information</h4>
            <form>
              <div class="mdl-cell mdl-cell--10-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                <input class="mdl-textfield__input" type="text" id="name" name="name" value="{{name}}">
                <label class="mdl-textfield__label" for="name">Name</label>
              </div>
              <div class="mdl-cell mdl-cell--10-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                <input class="mdl-textfield__input" type="text" id="surname" name="surname" value="{{surname}}">
                <label class="mdl-textfield__label" for="surname">Surname</label>
              </div>
              <div class="mdl-cell mdl-cell--12-col">
                <!--Gender-->
                <label class=" mdl-radio mdl-js-radio mdl-js-ripple-effect" for="option-1">
                  <input type="radio" id="option-1" class="mdl-radio__button" name="options" value="Male" checked>
                  <span class="mdl-radio__label">Male</span>
                </label>
                <label class=" mdl-radio mdl-js-radio mdl-js-ripple-effect" for="option-1">
                  <input type="radio" id="option-1" class="mdl-radio__button" name="options" value="Female" >
                  <span class="mdl-radio__label">Female</span>
                </label>
              </div>
              <div class="mdl-cell">
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                Button
                </button>
              </div>
            </form>
          </div>
          <!-- Preferences -->
          <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col">
            <h4 align="center">Preferences</h4>
            <div class="mdl-cell">
              <label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="">
                <input type="checkbox" id="" class="mdl-checkbox__input" checked>
                <span class="mdl-checkbox__label">Checkbox</span>
              </label>
            </div>
          </div>
        </main>
      </body>
    </html>