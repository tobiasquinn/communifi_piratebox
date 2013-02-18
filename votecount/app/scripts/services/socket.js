'use strict';

votecountApp.factory('socket', function($rootScope) {
    var socket = new SockJS('/vote');
    var callbacks = {};
    //socket.onopen = function() {
    //    console.log("onopen");
    //};
    socket.onmessage = function(mess) {
        console.log('onmessage', mess);
        // message dispatcher
    };
    // Public API here
    return {
        onopen: function(callback) {
            socket.onopen = function() {
                callback.apply();
            };
        },
        on: function(eventName, callback) {
            console.log("add callback", eventName);
            callbacks[eventName] = callback;
            //socket.onmessage = function() {
            //    console.log('onmessage')
            //    var args = arguments;
            //    //$rootScope.$apply(function() {
            //    //    callback.apply(socket, args);
            //    //});
            //};
        },
        emit: function(eventName, data, callback) {
            console.log("EMIT", eventName, data);
            if (data == undefined) socket.send(eventName);
            else socket.send(JSON.stringify({eventName: data}));//'TESTing');
            //socket.send({eventName: data});//, function () {
            //    var args = arguments;
            //    $rootScope.$apply(function () {
            //        if (callback) {
            //            callback.apply(socket, args);
            //        }
            //    });
            //})
        }
    };
});
