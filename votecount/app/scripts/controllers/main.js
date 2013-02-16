'use strict';

votecountApp.controller('MainCtrl', function($scope, $timeout, $http, socket) {
    // this should be sent from server?
    $scope.candidates = [
        { 'name': 'UP',         'btn': 'btn-success' },
        { 'name': 'NEUTRAL',    'btn': 'btn-warning' },
        { 'name': 'DOWN',       'btn': 'btn-danger' },
    ];

    // add vote count to candidates table
    for (var i=0; i < $scope.candidates.length; i++) {
        $scope.candidates[i]['votes'] = 0;
    }

    // realtime vote information from server
    $scope.voters = 'UNKNOWN';

    // local vote state
    $scope.yourvote = false;
    // debug - should be from server
    $scope.timeleft = 60;

    $scope.vote = function(vote) {
        $scope.yourvote = vote;
        socket.emit('vote', vote);
    };

    // incoming vote information
    // {
    //      'voters': number of connected voters,
    //      'votes': {
    //          candidate_name: number_of_votes
    //      }
    // }
    socket.on('voteinfo', function(data) {
        console.log("VOTEINFO");
        console.log(data);
        $scope.voters = data['voters'];
        // unpack our vote information
        console.log(data['votes']);
        // write our vote information in the scope
        for (var i=0; i < $scope.candidates.length; i++) {
            var votecount = data['votes'][$scope.candidates[i].name]; // FIXME: key failure...
            $scope.candidates[i].votes = votecount;
        }
    });

    /* voting time */
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
