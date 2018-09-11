export default class CameraController {
    constructor(camera) {
        this.camera = camera;

        let imageTopicIndex = camera.topics_list.findIndex(c => c[1] === "sensor_msgs/Image");

        this.camera.url = "http://localhost:8888/stream?topic=" + camera.topics_list[imageTopicIndex][0];
        console.log(camera);
    }
}
