export default function routes($stateProvider) {
    $stateProvider
        .state('cameras', {
            url: '/cameras',
            template: require('./cameras.html'),
            controller: 'CamerasController',
            controllerAs: 'cameras',
            resolve: {
                camerasResolved: function (CamerasService) {
                    return CamerasService.getCamerasList();
                }
            }
        });
}

routes.$inject = ['$stateProvider'];
