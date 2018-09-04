export default class CamerasController {
    constructor(cameras, rosService, $q) {
        console.log(cameras);
        this.camerasArray = cameras.cameras;
        this.rosService = rosService;
        this.$q = $q;

        for (let camera of this.camerasArray) {
            camera.url = CamerasController.makeCameraUrl(camera);
        }
    }

    add(camera) {
        let promise = this.rosService.addCamera(camera);

        this.$q.when(promise).then((result) => {
            alert(result.message);

            let camera = result.camera;
            camera.url = CamerasController.makeCameraUrl(camera);
            this.camerasArray.push(camera);
        });
    }

    remove(camera) {
        if (!Array.isArray(this.camerasArray) || !this.camerasArray.length) {
            return;
        }

        let promise = this.rosService.removeCamera(camera);

        this.$q.when(promise).then((result) => {
            alert(result.message);

            let index = this.camerasArray.indexOf(camera);
            if (index !== -1) {
                this.camerasArray.splice(index, 1);
            }
        });
    }

    static makeCameraUrl(camera) {
        if (Array.isArray(camera.topics_list) && camera.topics_list.length) {
            let imageTopicIndex = camera.topics_list.findIndex(c => c[1] == "sensor_msgs/Image");

            return "http://localhost:8888/stream?topic=" + camera.topics_list[imageTopicIndex][0];
        }
        return "";
    }
}

CamerasController.$inject = ['cameras', 'ros', '$q'];
