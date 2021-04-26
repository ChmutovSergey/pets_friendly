var myMap;

ymaps.ready(init);

function init () {
    var hotels = JSON.parse(document.getElementById('hotels-data').textContent);
    console.log(hotels)
    var center_map = JSON.parse(document.getElementById('center_map').textContent);

    myMap = new ymaps.Map('map', {
        center: center_map,
        zoom: 14,
        controls: ['routeButtonControl', 'fullscreenControl']
    }, {
        searchControlProvider: 'yandex#search'
    });

    for (let i = 0; i < hotels.length; i++) {
        myMap.geoObjects.add(new ymaps.Placemark(hotels[i].geo_point, {
            balloonContentHeader: '<a href = "#">' + hotels[i].title + '</a>',
            balloonContentBody: hotels[i].phone + '<br><b>Режим работы: ' + hotels[i].work_time + '</b>',
            balloonContentFooter: hotels[i].address
        }, {
            preset: 'islands#icon',
            iconColor: 'red'
        }))
    }
}
