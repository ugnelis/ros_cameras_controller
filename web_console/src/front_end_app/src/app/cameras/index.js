import angular from 'angular';
import uirouter from 'angular-ui-router';

import routing from './cameras.routes';
import CamerasController from './cameras.controller';
import ros from '../services/ros.service';

export default angular.module('app.cameras', [uirouter, ros])
    .config(routing)
    .controller('CamerasController', CamerasController)
    .name;
