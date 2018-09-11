import roslib from 'roslib';

export default class CamerasService {
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

    addCamera(camera) {
        let addCameraRequest = new roslib.ServiceRequest({
            command: "add",
            argument: camera.url
        });

        let promise = new Promise((resolve, reject) => {
            this.commanderClient.callService(
                addCameraRequest,
                (params) => resolve(JSON.parse(params.message)));
        });

        return promise;
    }

    removeCamera(camera) {
        let removeCameraRequest = new roslib.ServiceRequest({
            command: "remove",
            argument: camera.id
        });

        let promise = new Promise((resolve, reject) => {
            this.commanderClient.callService(
                removeCameraRequest,
                (params) => resolve(JSON.parse(params.message)));
        });

        return promise;
    }
}
