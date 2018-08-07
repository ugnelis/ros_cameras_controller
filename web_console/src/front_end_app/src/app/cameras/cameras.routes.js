// import ros from '../services/ros.service';
routes.$inject = ['$stateProvider'];

export default function routes($stateProvider) {
    $stateProvider
        .state('cameras', {
            url: '/cameras',
            template: require('./cameras.html'),
            controller: 'CamerasController',
            controllerAs: 'cameras',
            resolve: {
                cameras: function () {
                    return "123";
                    // return ros.getCamerasList();
                }
            }
        });
}
