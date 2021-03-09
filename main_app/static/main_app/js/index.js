ymaps.ready(init);
var request = new XMLHttpRequest();

function init() {
    var suggestView1 = new ymaps.SuggestView('input_address');
}

function getAddress() {
    var address = document.getElementById('input_address').value;
    var myGeocoder = ymaps.geocode(address, {results: 1});
    myGeocoder.then(
        function (res) {
            console.log('Все данные геообъекта: ', res.geoObjects.get(0).geometry.getCoordinates());
        },
        function (err) {
            console.log('Error');
        }
    );
}

function reqReadyStateChange() {
    if (request.readyState == 4 && request.status == 200)
        document.getElementById("output").innerHTML=request.responseText;
}


var body = "name=" + user.name + "&age="+user.age;
request.open("POST", "http://localhost:8080/postdata.php");
request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
request.onreadystatechange = reqReadyStateChange;
request.send(body);