function init() {
  var input = document.getElementById('location');
  var autocomplete = new google.maps.places.Autocomplete(input);
}

google.maps.event.addDomListener(window, 'load', init);


// http://stackoverflow.com/questions/13689705/how-to-add-google-maps-autocomplete-search-box
// https://developers.google.com/maps/documentation/javascript/examples/places-autocomplete