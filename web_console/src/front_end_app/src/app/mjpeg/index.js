import angular from 'angular';

import MjpegDirective from './mjpeg.directive';

export default angular.module('app.mjpeg', [])
    .directive('mjpeg', () => new MjpegDirective)
    .name;
