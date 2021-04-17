var myMap;

ymaps.ready(init);

function init () {
    var hotels = JSON.parse(document.getElementById('hotels-data').textContent);
    var center_map = JSON.parse(document.getElementById('center_map').textContent);

    myMap = new ymaps.Map('map', {
        center: center_map,
        zoom: 10
    }, {
        searchControlProvider: 'yandex#search'
    });

    for (let i = 0; i < hotels.length; i++) {
        myMap.geoObjects.add(new ymaps.Placemark(hotels[i].geo_point, {
            balloonContent: hotels[i].title
        }, {
            preset: 'islands#icon',
            iconColor: 'red'
        }))
    }
}
