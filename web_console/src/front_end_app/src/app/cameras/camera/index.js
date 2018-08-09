import angular from 'angular';
import uirouter from 'angular-ui-router';

import routing from './camera.routes';
import CameraController from './camera.controller';
import mjpeg from '../../directives/mjpeg.directive';

export default angular.module('app.camera', [uirouter, mjpeg])
    .config(routing)
    .controller('CameraController', CameraController)
    .name;
