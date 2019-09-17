function submit_message() {

    var title = document.getElementById("title");
    var message = document.getElementById("message");

    var entry = {
        title: title.value,
        message: message.value
    };

    fetch(`${window.location}/create-entry`, {
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