import angular from 'angular';
import uirouter from 'angular-ui-router';

import routing from './cameras.routes';
import CamerasController from './cameras.controller';
import CamerasService from './cameras.service';
import alert from '../alert';
import mjpeg from '../mjpeg';

export default angular.module('app.cameras', [uirouter, alert, mjpeg])
    .config(routing)
    .controller('CamerasController', CamerasController)
    .service('CamerasService', CamerasService)
    .name;
