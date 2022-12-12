var lat, lng
function initMap() 
{
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 19.076090, lng: 72.877426 },
    zoom: 11,
    mapID: '9cc9aa6e70199347'
  });

  marker = new google.maps.Marker({
    position: {lat: 19.110297651300932, lng: 72.83770156984905},
    map: map,
    draggable: true,
  });

  marker.addListener("drag", (mapsMouseEvent) => {
    lat = mapsMouseEvent.latLng.toJSON().lat
    lng = mapsMouseEvent.latLng.toJSON().lng
    lat = Number.parseFloat(lat).toFixed(6);
    lng = Number.parseFloat(lng).toFixed(6);
    document.getElementById('id_lat').setAttribute('value', lat);
    document.getElementById('id_long').setAttribute('value', lng);
  });
}