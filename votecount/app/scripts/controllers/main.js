'use strict';

votecountApp.controller('MainCtrl', function($scope) {
  $scope.yourvote = 'NEUTRAL';
  $scope.votes = 'UNKNOWN';
  $scope.count = {
    'up': 0,
    'down': 0,
    'neutral': 0,
  };

  var lastvote = 'NETURAL';

  $scope.vote = function(count) {
      switch(count) {
          case 1:
              $scope.count['up']++;
              lastvote = 'UP';
              break;
          case 0:
              $scope.count['neutral']++;
              lastvote = 'NEUTRAL';
              break;
          case -1:
              $scope.count['down']++;
              lastvote = 'DOWN';
              break;
      }
      $scope.yourvote = lastvote;
  }
});
