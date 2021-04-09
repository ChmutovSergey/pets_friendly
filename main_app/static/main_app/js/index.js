ymaps.ready(init);
var request = new XMLHttpRequest();

function init() {
    var suggestView1 = new ymaps.SuggestView('input_address');
}

function getGeoCode() {
    var address = document.getElementById('input_address').value;
    var myGeocoder = ymaps.geocode(address, {results: 1});

    myGeocoder.then(
        function (res) {
            var geo_code = res.geoObjects.get(0).geometry.getCoordinates();
            var params = `latitude=${geo_code[0]}&longitude=${geo_code[1]}`;

            document.location="/hotels?" + params;
        }
    );
}