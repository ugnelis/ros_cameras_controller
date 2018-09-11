export default class AlertService {
    constructor($rootScope) {
        this.$rootScope = $rootScope;

        this.alerts = [];
    }

    add(type, message) {
        if (type !== "success" && type !== "info" && type !== "warning" && type !== "danger")
            type = "info";

        if (Array.isArray(message))
            message.forEach(function (entry) {
                this.alerts.push({type: type, msg: entry});
            });
        else
            this.alerts.push({type: type, msg: message});
    }

    close(index) {
        this.alerts.splice(index, 1);
    }

    getAlerts() {
        return this.alerts;
    }

    clear() {
        this.alerts = [];
    }
}

AlertService.$inject = ['$rootScope'];