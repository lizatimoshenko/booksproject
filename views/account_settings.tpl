<form id="account-information" align="center">
  <h4>Настройки аккаунта</h4>
  </br>
  <div class="mdl-cell mdl-cell--10-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label ">
    <input class="mdl-textfield__input" type="text" id="username" name="username" value="{{username}}" readonly>
    <label class="mdl-textfield__label" for="username">Имя пользователя</label>
  </div>
  <div class="mdl-cell mdl-cell--10-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
    <input class="mdl-textfield__input" type="email" id="email" name="email" value="{{email}}">
    <label class="mdl-textfield__label" for="email">Электронная почта</label>
  </div>
  </br>
  <div class="mdl-cell mdl-cell--12-col">
    <div class=" mdl-cell mdl-cell--5-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
      <input class="mdl-textfield__input" type="password" id="password" name="password" value="">
      <label class="mdl-textfield__label" for="password">Новый пароль</label>
    </div>
    <div class=" mdl-cell mdl-cell--5-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
      <input class="mdl-textfield__input" type="password" id="confirm" name="confirm" value="">
      <label class="mdl-textfield__label" for="confirm">Подтвердите пароль</label>
    </div>
  </div>
  </br>
  <button onclick="changeAccountInfo()" style="float: right; margin-right:10%;" class=" mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
  Сохранить
  </button>
</form>