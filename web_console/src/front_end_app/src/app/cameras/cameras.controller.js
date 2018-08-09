export default class CamerasController {
    constructor(cameras) {
        console.log(cameras);
        this.camerasArray = cameras.cameras;

        for (let camera of this.camerasArray) {
            let imageTopicIndex = camera.topics_list.findIndex(c => c[1] == "sensor_msgs/Image");

            let cameraUrl = "http://localhost:8888/stream?topic=" + camera.topics_list[imageTopicIndex][0];
            camera.url = cameraUrl;
        }
    }
}
