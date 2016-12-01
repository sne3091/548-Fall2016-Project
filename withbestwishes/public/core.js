
angular.module('withBestWishes', [])
.controller('mainController', ['$scope','$http', function mainController($scope,$http) {
    $scope.formData = {};
    $scope.resultsVisible = false;
     // when submitting the add form, send the text to the node API
     $scope.fetchResults = function() {
        $http.post('/api/tweets', $scope.formData)
            .success(function(data) {
                $scope.formData = {}; // clear the form so our user is ready to enter another
                $scope.todos = data;
                $scope.resultsVisible =  $scope.resultsVisible ? false : true;
                console.log(data);
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };
}]);