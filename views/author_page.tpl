<html>
  <head>
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    % include('head.tpl', title=name)

  </head>
  <body>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      % include('header.tpl', title=name)
      <main class="mdl-layout__content mdl-color--grey-100">
        <div class="mdl-grid">
          <div class="mdl-cell mdl-cell--6-col">
            <ul class="demo-list-item mdl-list">
              <li class="mdl-list__item">

                <span class="mdl-list__item-primary-content">
                  Born: {{born}}
                </span>
              </li>
            </ul>
          </div>
          <div class="mdl-cell mdl-cell--6-col">
            <img src={{image}}>
          </div>

          <button onclick="myFunction()"  id="subscribe" class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">Subscribe
          </button>



        </div>
      </main>
    </div>

   <script>

  function myFunction(){
            var text = $('#subscribe').text();
            if (text == "Unsubscribe") {

         $.ajax({
            type: 'POST',
            url: '/unsubscribe_author',

            data: JSON.stringify(
            {'name': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function(res){

                   $('#subscribe').html('Subscribe');
                   console.log(res);
            },
             error: function (ajaxOptions, thrownError) {
                console.log("Error: Could not contact server.");
             }
         });


} else {

         $.ajax({
            type: 'POST',
            url: '/subscribe_author',

            data: JSON.stringify(
            {'name': $('#title').text()}
            ),
            contentType: "application/json",
            cache: false,
            processData: false,
            async: true,
            success: function(res){

                   $('#subscribe').html('Unsubscribe');
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