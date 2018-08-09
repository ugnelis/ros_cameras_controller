import 'bootstrap/dist/css/bootstrap.css';

import angular from 'angular';
import uirouter from 'angular-ui-router'

import '../style/app.css';

import routing from './app.config';
import home from './home';
import about from './about';
import cameras from './cameras';
import camera from './cameras/camera';

import ros from './services/ros.service';


angular.module('app', [uirouter, home, about, cameras, camera, ros])
    .config(routing);
