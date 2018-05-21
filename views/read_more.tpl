<html>
  <head>
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    % include('head.tpl', title=title)

  </head>
  <body>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title=title)
      <main class="mdl-layout__content mdl-color--grey-100">
        <div class="mdl-grid">
          <div class="mdl-cell mdl-cell--6-col">
            <ul class="demo-list-item mdl-list">
              <li class="mdl-list__item">

                <span class="mdl-list__item-primary-content">
                  Author:  <a href="/about_author/{{author}}"> {{author}}</a>
                </span>
              </li>
              <li class="mdl-list__item">
                <span class="mdl-list__item-primary-content">
                  Published: {{published}}
                </span>
              </li>
              <li class="mdl-list__item">
                <span class="mdl-list__item-primary-content">
                  Language: {{language}}
                </span>
              </li>
              <li class="mdl-list__item">
                <span class="mdl-list__item-primary-content">
                  Annotation : {{annotation}}
                </span>
              </li>
            </ul>
          </div>
          <div class="mdl-cell mdl-cell--6-col">
            <img src={{image}}>
          </div>

          <button onclick="myFunction()"  id="wish" class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
Add to wishlist
</button>


          <button onclick="readFunction()" id="read" class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
  Read
</button>

        </div>
      </main>
    </div>
    <script>

  function myFunction(){
            var text = $('#wish').text();
            if (text == "Delete") {

         $.ajax({
            type: 'POST',
            url: '/delete_wish',

            data: JSON.stringify(
            {'title': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function(res){

                   $('#wish').html('Add to wishes');
                   console.log(res);
            },
             error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
             }
         });


} else {

         $.ajax({
            type: 'POST',
            url: '/add_wish',

            data: JSON.stringify(
            {'title': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function(res){

                   $('#wish').html('Delete');
                   console.log(res);
            },
             error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
             }
         });

     };
     }

     function readFunction(){
            var text = $('#read').text();
            if (text == "Unread") {

         $.ajax({
            type: 'POST',
            url: '/unread_book',

            data: JSON.stringify(
            {'title': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function(res){

                   $('#read').html('Read');
                   console.log(res);
            },
             error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
             }
         });


} else {

         $.ajax({
            type: 'POST',
            url: '/read_book',

            data: JSON.stringify(
            {'title': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function(res){

                   $('#read').html('Unread');
                   console.log(res);
            },
             error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
             }
         });

     };
     }
</script>
  </body>

</html>