var myMap;

// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);

function init () {
    console.log(hotels);
    // Создание экземпляра карты и его привязка к контейнеру с
    // заданным id ("map").
    myMap = new ymaps.Map('map', {
        // При инициализации карты обязательно нужно указать
        // её центр и коэффициент масштабирования.
        center: [55.76, 37.64], // Москва
        zoom: 10
    }, {
        searchControlProvider: 'yandex#search'
    });

    myMap.geoObjects
        .add(new ymaps.Placemark([55.784415, 37.737291], {
            balloonContent: '<strong>BookingCat м. Партизанская</strong>'
        }, {
            preset: 'islands#icon',
            iconColor: 'red'
        }))
        .add(new ymaps.Placemark([55.922621, 37.427830], {
            balloonContent: '<strong>Отель "Планета Кошек"</strong>'
        }, {
            preset: 'islands#icon',
            iconColor: 'red'
        }))
}
