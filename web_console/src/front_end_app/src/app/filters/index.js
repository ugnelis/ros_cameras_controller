import angular from 'angular';
import uirouter from 'angular-ui-router';

import routing from './filters.routes';
import FiltersController from './filters.controller';
import FiltersService from './filters.service';
import CamerasService from '../cameras';
import alert from '../alert';
import mjpeg from '../mjpeg';

export default angular.module('app.filters', [uirouter, alert, mjpeg])
    .config(routing)
    .controller('FiltersController', FiltersController)
    .service('FiltersService', FiltersService)
    .name;
