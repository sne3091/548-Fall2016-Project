
angular.module('withBestWishes', ['ui.bootstrap'])
.controller('mainController', ['$scope','$http', function mainController($scope,$http) {
    $scope.formData = {};
    $scope.resultsVisible = false;
     // when submitting the add form, send the text to the node API
     $scope.fetchResults = function() {
        $http.post('/api/getItems', $scope.formData)
        .success(function(data) {
            $scope.resultsVisible = true;
            $scope.currentItems = data;
        })
        .error(function(data) {
            console.log('Error: ' + data);
        });
    };
}]);