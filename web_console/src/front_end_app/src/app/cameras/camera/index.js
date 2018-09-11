import angular from 'angular';
import uirouter from 'angular-ui-router';

import routing from './camera.routes';
import CameraController from './camera.controller';
import CamerasService from '../';
import mjpeg from '../../mjpeg';

export default angular.module('app.camera', [CamerasService, uirouter, mjpeg])
    .config(routing)
    .controller('CameraController', CameraController)
    .name;
