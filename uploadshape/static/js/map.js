
    $(document).ready(function(){
      var mapOptions = {
        center: new google.maps.LatLng(37.950902,23.641103),
        zoom: 7,
        mapTypeId: google.maps.MapTypeId.ROADMAP

      };
      map = new google.maps.Map(document.getElementById("map"), mapOptions);
      var infowindow = new google.maps.InfoWindow();
      var markers = [];
      var bounds = new google.maps.LatLngBounds();
      // var promise = $.getJSON("/get_geo/"); //same as map.data.loadGeoJson();
  		// 	promise.then(function(data){
      //     console.info(data);
  		// 		cachedGeoJson = data; //save the geojson in case we want to update its values
  		// 		map.data.addGeoJson(cachedGeoJson,{idPropertyName:"id"});
  		// 	});
      function get_data(){
        $.ajax({
          url: '/get_geo/',
          type: 'get',
          dataType: 'json',
          success: function (data) {
            console.info(data);

            map.data.addGeoJson(data,{idPropertyName:"id"});
          },
          complete: function (data) {
                   // Schedule the next
                   setTimeout(get_data, 1000);
           }
        })


      }
      setTimeout(get_data, 1000);
  })
