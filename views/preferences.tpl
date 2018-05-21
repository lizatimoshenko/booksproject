<form id="preferences">
    <h4 align="center">Предпочтeния</h4>
    <div class="mdl-cell mdl-cell--12-col">
        % count = 0
        % for genre_title in genres:
        <label class=" mdl-cell mdl-cell--5-col mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="{{count}}">
            % if preferences is not None:
            % if genre_title in preferences:
            <input type="checkbox" id="{{count}}" class="mdl-checkbox__input" value="{{genre_title}}" checked>
            % else:
            <input type="checkbox" id="{{count}}" class="mdl-checkbox__input" value="{{genre_title}}">
            % end
            % else:
            <input type="checkbox" id="{{count}}" class="mdl-checkbox__input" value="{{genre_title}}">
            %end
            <span class="mdl-checkbox__label">{{genre_title}}</span>
        </label>
        % count = count + 1
        % end
    </div>
    <div class="mdl-cell mdl-cell--middle">
        </br>
        <button onclick="addPreferences()"
                class="mdl-cell--6-col mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
            Сохранить
        </button>
    </div>
</form>