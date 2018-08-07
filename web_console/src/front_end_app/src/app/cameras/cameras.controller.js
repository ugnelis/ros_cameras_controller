export default class CamerasController {
    constructor(cameras) {
        let camerasIdArray = cameras.cameras;
        this.camerasUrlArray = [];

        for (const cameraId of camerasIdArray) {
            let cameraUrl = "http://localhost:8888/stream?topic=/" + cameraId + "/video_stream_to_topic/stream/image";
            this.camerasUrlArray.push(cameraUrl);
        }
    }
}
