
angular.module('withBestWishes', [])
.controller('mainController', ['$scope','$http', function mainController($scope,$http) {
    $scope.formData = {};
    $scope.resultsVisible = false;
     // when submitting the add form, send the text to the node API
     $scope.fetchResults = function() {
        $http.post('/api/getItems', $scope.formData)
            .success(function(data) {
                $scope.resultsVisible =  $scope.resultsVisible ? false : true;
                $scope.items = data;
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };
}]);