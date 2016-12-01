
angular.module('withBestWishes', [])
.controller('mainController', ['$scope','$http', function mainController($scope,$http) {
    $scope.formData = {};
    $scope.resultsVisible = false;
     // when submitting the add form, send the text to the node API
     $scope.fetchResults = function() {
        $http.post('/api/tweets', $scope.formData)
            .success(function(data) {
                $scope.formData = {}; // clear the form so our user is ready to enter another
                var domain_nba = ['LA Lakers','New York Knicks','Chicago Bulls','Golden State Warriors','San Antonio Spurs','Michael Jordan',
                'Stephen Curry','Kobe Bryant','Joakim Noah','Tim Duncan'];
                var domain_nfl = ['New England Patriots','Seattle Seahawks','Carolina Panthers','Dallas Cowboys','Denver Broncos','Tom Brady',
                'Cam Newton','Russell Wilson','Dak Prescott','Peyton Manning'];
                var domain_soccer = ['LA Lakers','New York Knicks','Chicago Bulls','Golden State Warriors','San Antonio Spurs','Michael Jordan',
                'Stephen Curry','Kobe Bryant','Joakim Noah','Tim Duncan'];
                var domain_nfl = ['New England Patriots','Seattle Seahawks','Carolina Panthers','Dallas Cowboys','Denver Broncos','Tom Brady',
                'Cam Newton','Russell Wilson','Dak Prescott','Peyton Manning'];
                for (var i = data.users.length - 1; i >= 0; i--) {
                    console.log(data.users[i].name);
                }
                $scope.resultsVisible =  $scope.resultsVisible ? false : true;
                console.log(data);
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };
}]);