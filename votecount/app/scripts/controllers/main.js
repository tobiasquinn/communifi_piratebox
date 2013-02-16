'use strict';

votecountApp.controller('MainCtrl', function($scope, $timeout, $http, socket) {
    $scope.yourvote = false;
    $scope.voters = 'UNKNOWN';
    $scope.timeleft = 60;

    $scope.vote = function(vote) {
        $scope.yourvote = vote;
        socket.emit('vote', vote);
    };

    socket.on('voteinfo', function(data) {
        console.log("VOTEINFO");
        console.log(data);
        $scope.voters = data['voters'];
    });

    var interval = 1000;
    //$http.get('/votingtime').success(function(data) {
    //    console.log("GOT");
    //    console.log(data);
    //    $scope.timeleft = data['time'];
    //    var mytimeout = $timeout($scope.onTimeout, interval);
    //});
    $scope.onTimeout = function() {
        $scope.timeleft--;
        if ($scope.timeleft > 0) {
            var mytimeout = $timeout($scope.onTimeout, interval);
        }
    }
    
    // nudge server
    socket.emit('connect');
});
