var app = angular.module('spotify').
controller('MainCtrl', function($scope, $http) {
  $scope.gender;
  $scope.age;
  $scope.customTrackList = {};
  function initCustom(){
    var responsePromise = $http.get("resources/spotify/customTracks.json");
    responsePromise.success(function(data, status, headers, config) {
        $scope.customTrackList = data;
        for each (track in customTrackList ){
          console.log(track[0]);
        }
    });
    responsePromise.error(function(data, status, headers, config) {
       console.log("AJAX failed!");
    });
  }
  initCustom();

});