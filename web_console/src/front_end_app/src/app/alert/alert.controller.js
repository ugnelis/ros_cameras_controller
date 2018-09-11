export default class AlertController {
    constructor(alertService) {
        this.alertService = alertService;

        this.alerts = this.alertService.getAlerts();
    }

    close(index) {
        this.alertService.close(index);
    }
}

AlertController.$inject = ['AlertService'];