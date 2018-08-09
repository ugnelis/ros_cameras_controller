import angular from 'angular';
import uirouter from 'angular-ui-router';

import routing from './about.routes'
import AboutController from './about.controller';

export default angular.module('app.about', [uirouter])
    .config(routing)
    .controller('AboutController', AboutController)
    .name;
