function initMap() {
    var myOptions = {
        zoom: 1,
        center: new google.maps.LatLng(0,0),
        mapTypeId: google.maps.MapTypeId.HYBRID
    };
    //map
    map = new google.maps.Map(document.getElementById("map"), myOptions);

    // i needed many markers so i used marker manager
    mgr = new MarkerManager(map);
    google.maps.event.addListener(mgr, "loaded", function() {
        // the data passed to the marker manager (is the array of) the coordinates of the locations and name + country

        for (var loc_info = 0; loc_info < all_locations.length; loc_info++) {


            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(all_locations[loc_info][0], all_locations[loc_info][1]),
                title: all_locations[loc_info][2]
            });
            mgr.addMarker(marker, 0);
        }
        mgr.refresh();
    });
}
google.maps.event.addDomListener(window, "load", initMap);
//thanks a lot to the selected answer here http://stackoverflow.com/questions/7819209/google-map-marker-manager-v3