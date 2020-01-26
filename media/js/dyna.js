var connection = new WebSocket('ws://' + location.host + '/ss/');

connection.onopen = function() {
    console.log("connection opened");
}

connection.onmessage = function(evt) {
    document.getElementById("demo").innerHTML = evt.data;
}

function manage(username) {
    if (username == "") {
        console.log("Field is required");
        // document.getElementById("demo").innerHTML = "Field is required";
    }
    
    if (connection.readyState == 1) {
        connection.send(username);
    } else {
        console.log("connection closed");
    }
}
