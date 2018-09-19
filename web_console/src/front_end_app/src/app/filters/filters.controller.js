export default class FiltersController {
    constructor(camerasResolved, filterTypesResolved, filtersService, alertService, $q) {
        this.camerasArray = camerasResolved.cameras;
        this.filtersService = filtersService;
        this.alertService = alertService;
        this.$q = $q;

        for (let camera of this.camerasArray) {
            for (let filter of camera.filters) {
                console.log(filter);
                filter.localUrl = FiltersController.makeStreamUrl(filter);
            }
        }

        console.log(this.camerasArray)
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
