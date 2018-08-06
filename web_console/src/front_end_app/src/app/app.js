import 'bootstrap/dist/css/bootstrap.css';

import angular from 'angular';
import uirouter from 'angular-ui-router'

import '../style/app.css';

import routing from './app.config';
import home from './home';
import about from './about';

angular.module('app', [uirouter, home, about])
    .config(routing);
