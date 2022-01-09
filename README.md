# myfirstsandbox

Live demo: http://timothyholmes.com.au/sand (Passenger might take a while to initialise app)

- Bootstrap (front end)
- Flask (web service)
- SQLite, SQLAlchemy (DB and object relational mapper)

Another CRUD application put together to learn how to use REST API calls from the frontend. Done with the intention of implementing in timothy-holmes/superaudit.

Creating a new post:
```javascript
function submit_message() {

    var title = document.getElementById("title");
    var message = document.getElementById("message");

    var entry = {
        title: title.value,
        message: message.value
    };
    
    fetch(`${url_for_create_entry}`, {  // use global var defined in base.html
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({"content-type": "application/json"})
    })
    .then(function (response) {
        if (response.status !== 200) {
            console.log(`Looks like there was a problem. Status code: ${response.status}`);
            return;
        }
        response.text().then(function (data) {
            title.value = "";
            message.value = "";
            $( data ).appendTo( ".sandbox" );
            console.log(data);
        });
    })
    .catch(function(error) {console.log("Fetch error: " + error);
    });   
}
```

I like this trick. Force the browser to reload a .js file that's been updated since the last page load by attaching a truncated checksum to the URI.
```python
def index():
    ...
    return render_template(
        ...
        js_version=get_js_version_hash()
        )
```
```html
<script src="/sand/static/js/submit.js?version=f1c950b1"></script>
```
