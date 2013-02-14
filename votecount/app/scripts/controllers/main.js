'use strict';

votecountApp.controller('MainCtrl', function($scope, $timeout) {
    $scope.yourvote = false;
    $scope.votes = 'UNKNOWN';
    $scope.timeleft = 60;

    $scope.vote = function(vote) {
        $scope.yourvote = vote;
        $scope.count[vote]++;
    };

    var interval = 1000;
    $scope.onTimeout = function() {
        $scope.timeleft--;
        if ($scope.timeleft > 0) {
            mytimeout = $timeout($scope.onTimeout, interval);
        }
    }
    var mytimeout = $timeout($scope.onTimeout, interval);
});
