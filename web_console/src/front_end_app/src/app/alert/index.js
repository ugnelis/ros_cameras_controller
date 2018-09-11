import angular from 'angular';

import AlertController from './alert.controller';
import AlertDirective from './alert.directive';
import AlertService from './alert.service';

export default angular.module('app.alert', [])
    .controller('AlertController', AlertController)
    .directive('alertbox', () => new AlertDirective)
    .service('AlertService', AlertService)
    .name;
