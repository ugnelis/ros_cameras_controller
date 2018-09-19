import roslib from 'roslib';

export default class FiltersService {
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

    getFilterTypes() {
        let getFilterTypesRequest = new roslib.ServiceRequest({
            command: "filter.types",
            arguments: []
        });

        let promise = new Promise((resolve, reject) => {
            this.commanderClient.callService(
                getFilterTypesRequest,
                (params) => resolve(JSON.parse(params.message)));
        });

        return promise;
    }

    addFilter(camera, filterType) {
        let addFilterRequest = new roslib.ServiceRequest({
            command: "filter.add",
            arguments: [camera.url, filterType]
        });

        let promise = new Promise((resolve, reject) => {
            this.commanderClient.callService(
                addFilterRequest,
                (params) => resolve(JSON.parse(params.message)));
        });

        return promise;
    }

    removeFilter(camera, filter) {
        let removeCameraRequest = new roslib.ServiceRequest({
            command: "filter.remove",
            arguments: [camera.id, filter.id]
        });

        let promise = new Promise((resolve, reject) => {
            this.commanderClient.callService(
                removeCameraRequest,
                (params) => resolve(JSON.parse(params.message)));
        });

        return promise;
    }
}
