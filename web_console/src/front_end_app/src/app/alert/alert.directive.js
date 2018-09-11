export default class AlertDirective {
    constructor() {
        this.restrict = 'A';
        this.scope = {};
        this.controller = 'AlertController';
        this.controllerAs = "alertbox";
        this.template = require('./alert.html');
    }
}
