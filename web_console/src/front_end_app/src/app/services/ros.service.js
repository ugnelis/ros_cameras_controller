import angular from 'angular';
import roslib from 'roslib';

class ROS {
    constructor() {
        // Create a connection to the rosbridge WebSocket server.
        this.ros = new roslib.Ros();

        this.ros.on('connection', function() {
            console.log('ROS connection made!');
        });

        this.ros.on('error', function(error) {
            console.log(error);
        });

        this.ros.on('close', function() {
            console.log('ROS connection closed.');
        });

        this.ros.connect('ws://localhost:9090');

        this.commanderClient = new roslib.Service({
            ros : this.ros,
            name : '/commander',
            serviceType : 'commander'
        });
    }

    printCamerasList() {
        let listCamerasRequest = new roslib.ServiceRequest({
            command : "list",
            argument : ""
        });

        this.commanderClient.callService(listCamerasRequest, function(result) {
            console.log(result.message);
        });
    }
}

export default angular.module('services.ros', [])
    .service('ros', ROS)
    .name;