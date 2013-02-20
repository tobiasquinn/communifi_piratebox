'use strict';

votecountApp.controller('MainCtrl', function($scope, $timeout, $http, socket) {
    // candidates list is fetched from server
    $scope.candidates = [];
    // this should be sent from server?
    socket.on('candidates', function(data) {
        console.log("CANDIDATES", data);
        // some styles to colour our buttons
        var button_styles = ['btn-success', 'btn-warning', 'btn-danger'];
        var i = 0;
        data = _.map(data, function(c) {
            return {
                'name': c,
                'btn': button_styles[i++ % button_styles.length],
                'votes': 0
            }
        });
        $scope.candidates = data;
    });

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
            var votecount = data['votes'][$scope.candidates[i].name];
            // we may not get the full list, assume votecount is 0
            votecount = (votecount == undefined ? 0 : votecount);
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
    
    // nudge server on socket connect
    socket.onopen(function() {
        socket.emit('connect');
    });
});
