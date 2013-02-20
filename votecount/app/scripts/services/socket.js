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
            console.log("socket.js::on::add callback", eventName);
            callbacks[eventName] = callback;
        },
        emit: function(eventName, data, callback) {
            console.log("socket.js::emit", eventName, data);
            var obj = {
                name: eventName,
                data: data
            };
            socket.send(JSON.stringify(obj));
        }
    };
});
