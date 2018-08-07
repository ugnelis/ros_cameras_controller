import angular from 'angular';
import uirouter from 'angular-ui-router';

import routing from './cameras.routes';
import CamerasController from './cameras.controller';

export default angular.module('app.cameras', [uirouter])
    .config(routing)
    .controller('CamerasController', CamerasController)
    .name;
