export default class CamerasController {
    constructor(cameras, rosService) {
        console.log(cameras);
        this.camerasArray = cameras.cameras;
        this.rosService = rosService;

        for (let camera of this.camerasArray) {
            camera.url = CamerasController.makeCameraUrl(camera);
        }

        console.log(this);
        this.add = this.add.bind(this);
    }

    add(camera) {
        console.log(camera);
        let promise = this.rosService.addCamera(camera);

        let self = this;
        promise.then((params) => {
            alert(params.message);
            // TODO(Ugnelis): fix here. It doesn't update.
            console.log(params);
            let camera = params.camera;
            camera.url = CamerasController.makeCameraUrl(camera);
            self.camerasArray.push(camera);
        });
    }

    remove(camera) {
        console.log(this.camerasArray);

        if (!Array.isArray(this.camerasArray) || !this.camerasArray.length) {
            return;
        }

        this.camerasArray.pop();
        console.log(this.camerasArray);

        // let promise = this.rosService.removeCamera(camera);
        //
        // let self = this;
        // promise.then((params) => {
        //     alert(params.message);
        //     let camera = params.camera;
        //     camera.url = CamerasController.makeCameraUrl(camera);
        //     self.camerasArray.push(camera);
        //
        //     self
        // });
    }

    static makeCameraUrl(camera) {
        if (Array.isArray(camera.topics_list) && camera.topics_list.length) {
            let imageTopicIndex = camera.topics_list.findIndex(c => c[1] == "sensor_msgs/Image");

            return "http://localhost:8888/stream?topic=" + camera.topics_list[imageTopicIndex][0];
        }
        return "";
    }
}

CamerasController.$inject = ['cameras', 'ros'];
