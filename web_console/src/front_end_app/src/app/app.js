import 'bootstrap/dist/css/bootstrap.css';

import angular from 'angular';
import uirouter from 'angular-ui-router'
import uibootstrap from 'angular-ui-bootstrap'

import '../style/app.css';

import routing from './app.config';
import home from './home';
import about from './about';
import cameras from './cameras';
import camera from './cameras/camera';
import filters from './filters';


angular.module('app', [
    uirouter,
    uibootstrap,
    home,
    about,
    cameras,
    camera,
    filters
])
    .config(routing);
