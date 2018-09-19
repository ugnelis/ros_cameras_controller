export default class CameraController {
    constructor(cameraResolved) {
        this.camera = cameraResolved.camera;

        let imageTopicIndex = this.camera.topics_list.findIndex(c => c[1] === "sensor_msgs/Image");

        this.camera.localUrl = "http://localhost:8888/stream?topic=" + this.camera.topics_list[imageTopicIndex][0];
    }
}

