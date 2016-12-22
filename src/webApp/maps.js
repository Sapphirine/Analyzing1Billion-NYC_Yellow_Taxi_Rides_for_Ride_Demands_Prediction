var currentdate = new Date();
var choosedLocation = [40.807468,-73.962100];
var choosedTime = [currentdate.getHours(), currentdate.getMinutes()];
var currentWeather;

angular.module('myapp', ['ngMap']).run(function($rootScope) {
  $rootScope.$on('mapInitialized', function(evt,map) {
    $rootScope.map = map;
    $rootScope.$apply();
  });
})

.controller('testCtrl', ['$scope', function testCtrl($scope) {
  $scope.latlng = [40.73267350647168,-73.99295210838318];
  $scope.getpos = function(event){
     $scope.latlng = [event.latLng.lat(), event.latLng.lng()];
     choosedLocation = $scope.latlng;
     console.log("Location is: " + choosedLocation);
  };
  
}])

.controller('timeCtrl', ['$scope', function timeCtrl($scope) {
	$scope.time = choosedTime;
	$scope.timeHour = $scope.time[0];
	$scope.timeMinute = $scope.time[1];

	$scope.changeTimeFunction = function() {

		hour = $scope.timeHour;
		minute = $scope.timeMinute;

		// check if hour is out of range
		hour %= 24;
		minute %= 60;
		if (hour < 0)	hour += 24;
		if (minute < 0) minute += 60;

		$scope.time = [hour, minute];
		choosedTime = $scope.time;
    $scope.timeHour = hour;
    $scope.timeMinute = minute;

	}

	$scope.getCurrentTime = function() {
		console.log("reset current time");
		currentdate = new Date();
		choosedTime = [currentdate.getHours(), currentdate.getMinutes()];
		$scope.time = choosedTime;
    $scope.timeHour = choosedTime[0];
    $scope.timeMinute = choosedTime[1];
	}

	$scope.sendParameter = function() {
		console.log('Send time and location here: ');
		console.log('Location is -- ' + choosedLocation);
		console.log('Time is -- ' + choosedTime);
    console.log('Weather is -- ' + currentWeather);
	}

}])

.controller('WeatCtrl', function WeatCtrl($http) {
  
  var vm = this;
  
  var URL = 'http://api.openweathermap.org/data/2.5/forecast/daily';
  
  var request = {
    method: 'GET',
    url: URL,
    params: {
       q: 'NewYork',
      mode: 'json',
      units: 'imperial',
      cnt: '7',
      appid: '**********'
    }
  };
  
  $http(request)
    .then(function(response) {
      vm.data = response.data;
      vm.aveTemp = (vm.data.list[0].temp.min + vm.data.list[0].temp.max)/2;
      // Accuracy controll
      vm.aveTemp = (vm.aveTemp).toFixed(2);
      vm.main = vm.data.list[0].weather[0].main;
      currentWeather = [vm.aveTemp, vm.main];
      console.log(vm.data);
      console.log(currentWeather);
    }).
    catch(function(response) {
      vm.data = response.data;
    });
})


.controller('PredCtrl', ['$http', '$scope', function PredCtrl($http, $scope) {

  $scope.resultArea = '--';
  $scope.resultRide = '--';
  $scope.resultFare = '--';
  $scope.resultTips = '--';
    
  var URL = 'https://********.execute-api.us-east-1.amazonaws.com/dep0/predict-customer-number';
  
  var request = {
    method: 'POST',
    url: URL,
    data: {
      "hours": "3",
      "const": "1",
      "balns": "0"
    }
  };

  $scope.sendRequest = function() {
    console.log('Send time and location here: ');
    console.log('Location is -- ' + choosedLocation);
    console.log('Time is -- ' + choosedTime);
    console.log('Weather is -- ' + currentWeather);

    request.data["hours"] = choosedTime;
    request.data["const"] = choosedLocation;
    request.data["balns"] = currentWeather;

    console.log(request.data);
    
    $http(request)
    .then(function(response) {
      var rsp_data_area = response.data['location_area'];
      var rsp_data_ride = response.data['predict_ride_num'];
      var rsp_data_fare = response.data['predict_ride_fare'];
      var rsp_data_tips = response.data['predict_ride_tips'];
      // var len = rsp_data.length;
      // rsp_data = rsp_data.substring(1, len-1);
      console.log(response.data); 

      $scope.resultArea = rsp_data_area;
      $scope.resultRide = rsp_data_ride;
      $scope.resultFare = rsp_data_fare;
      $scope.resultTips = rsp_data_tips;
    }).
    catch(function(response) {
      console.log(response.data);
      $scope.resultArea = "Ooops, Error";
    });
  }
   
}]);
