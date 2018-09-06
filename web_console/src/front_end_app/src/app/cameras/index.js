import angular from 'angular';
import uirouter from 'angular-ui-router';

import routing from './cameras.routes';
import CamerasController from './cameras.controller';
import mjpeg from '../directives/mjpeg.directive';
import ros from '../services/ros.service';

export default angular.module('app.cameras', [uirouter, mjpeg])
    .config(routing)
    .controller('CamerasController', CamerasController)
    .name;
