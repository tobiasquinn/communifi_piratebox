'use strict';

votecountApp.factory('socket', function($rootScope) {
    var socket = new SockJS('/vote');
    var callbacks = {};
    socket.onmessage = function(mess) {
        // quick and dirty message dispatcher
        var message_type = Object.keys(mess.data)[0];
        var message_data = mess.data[message_type];
        var func = callbacks[message_type];
        $rootScope.$apply(function() {
            func.call(socket, message_data);
        });
    };
    // Public API here
    return {
        onopen: function(callback) {
            socket.onopen = function() {
                callback.apply(socket);
            };
        },
        on: function(eventName, callback) {
            // FIXME: only one on message type callback per socket connection
            console.log("add callback", eventName);
            callbacks[eventName] = callback;
        },
        emit: function(eventName, data, callback) {
            console.log("EMIT", eventName, data);
            if (data == undefined) {
                socket.send(eventName);
            } else {
                var obj = {};
                obj[eventName] = data;
                socket.send(JSON.stringify(obj));
            }
        }
    };
});
