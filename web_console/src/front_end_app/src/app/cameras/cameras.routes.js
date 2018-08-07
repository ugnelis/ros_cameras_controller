routes.$inject = ['$stateProvider'];

export default function routes($stateProvider, ros) {
    $stateProvider
        .state('cameras', {
            url: '/cameras',
            template: require('./cameras.html'),
            controller: 'CamerasController',
            controllerAs: 'cameras',
            resolve: {
                cameras: function (ros) {
                    return ros.getCamerasList();
                }
            }
        });
}
