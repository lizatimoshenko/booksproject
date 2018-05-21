<form enctype='multipart/form-data' align="center" >
  <div class="mdl-cell mdl-cell--12-col" >
    <h4>Персональные данные</h4>
    <img class="mdl-cell mdl-cell--4-col" id="avatar" src={{avatar}}  width="100" height="100"/>
    <label class="mdl-button mdl-button--colored mdl-js-button mdl-button--raised mdl-js-ripple-effect">
      Выбрать<input type="file" id="upload" name="upload" style="display: none;">
    </label>
    <div class=" mdl-cell mdl-cell--5-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
      <input class="mdl-textfield__input" type="text" name="uploadFile" id="uploadFile" readonly/>
      <label class="mdl-textfield__label" for="uploadFile">Изображение </label>
    </div>
  </div>
  <div class="mdl-cell mdl-cell--10-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
    % if name is None:
    <input class="mdl-textfield__input" type="text" id="name" name="name" value="">
    %end
    % if name is not None:
    <input class="mdl-textfield__input" type="text" id="name" name="name" value="{{name}}">
    %end
    <label class="mdl-textfield__label" for="name">Имя</label>
  </div>
  <div class="mdl-cell mdl-cell--10-col mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
    % if surname is None:
    <input class="mdl-textfield__input" type="text" id="surname" name="surname" value="">
    %end
    % if surname is not None:
    <input class="mdl-textfield__input" type="text" id="surname" name="surname" value="{{surname}}">
    %end
    <label class="mdl-textfield__label" for="surname">Фамилия</label>
  </div>
  </br>
  <button onclick="changePersonalData()" style="float: right; margin-right:10%;" class=" mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
  Сохранить
  </button>
</form>