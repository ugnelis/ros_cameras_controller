export default class FiltersController {
    constructor(camerasResolved, filterTypesResolved, filtersService, alertService, $q) {
        this.camerasArray = camerasResolved.cameras;
        this.filtersService = filtersService;
        this.alertService = alertService;
        this.$q = $q;

        for (let camera of this.camerasArray) {
            for (let filter of camera.filters) {
                filter.localUrl = FiltersController.makeStreamUrl(filter);
            }
        }
    }

    removeFilter(camera, filter) {
        if (!confirm("Are you sure?")) {
            return;
        }

        if (!Array.isArray(this.camerasArray) || !this.camerasArray.length) {
            return;
        }

        let promise = this.filtersService.removeFilter(camera, filter);

        this.$q.when(promise).then((result) => {
            if (result.code !== 200) {
                this.alertService.add("danger", result.message);
                return;
            }

            this.alertService.add("success", result.message);

            let cameraIndex = this.camerasArray.indexOf(camera);
            if (cameraIndex === -1) {
                return;
            }

            let filterIndex = this.camerasArray[cameraIndex].filters.indexOf(filter);
            if (filterIndex !== -1) {
                this.camerasArray[cameraIndex].filters.splice(filterIndex, 1);
            }
        });
    }


    static makeStreamUrl(filter) {
        if (Array.isArray(filter.topics_list) && filter.topics_list.length) {
            let imageTopicIndex = filter.topics_list.findIndex(c => c[1] === "sensor_msgs/Image");

            return "http://localhost:8888/stream?topic=" + filter.topics_list[imageTopicIndex][0];
        }
        return "";
    }
}

FiltersController.$inject = ['camerasResolved', 'filterTypesResolved', 'FiltersService', 'AlertService', '$q'];
