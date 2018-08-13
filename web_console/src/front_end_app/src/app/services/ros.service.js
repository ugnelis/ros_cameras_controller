import angular from 'angular';
import roslib from 'roslib';

class ROS {
    constructor() {
        // Create a connection to the rosbridge WebSocket server.
        this.ros = new roslib.Ros();

        this.ros.on('connection', function () {
            console.log('ROS connection made!');
        });

        this.ros.on('error', function (error) {
            console.log(error);
        });

        this.ros.on('close', function () {
            console.log('ROS connection closed.');
        });

        this.ros.connect('ws://localhost:9090');

        this.commanderClient = new roslib.Service({
            ros: this.ros,
            name: '/commander',
            serviceType: 'commander'
        });
    }

    getCamerasList() {
        let listCamerasRequest = new roslib.ServiceRequest({
            command: "list",
            argument: ""
        });

        let promise = new Promise((resolve, reject) => {
            this.commanderClient.callService(
                listCamerasRequest,
                (params) => resolve(JSON.parse(params.message)));
        });

        return promise;
    }

    getCamera(id) {
        let getCameraRequest = new roslib.ServiceRequest({
            command: "get",
            argument: id
        });

        let promise = new Promise((resolve, reject) => {
            this.commanderClient.callService(
                getCameraRequest,
                (params) => resolve(JSON.parse(params.message)));
        });

        return promise;
    }
}

export default angular.module('services.ros', [])
    .service('ros', ROS)
    .name;