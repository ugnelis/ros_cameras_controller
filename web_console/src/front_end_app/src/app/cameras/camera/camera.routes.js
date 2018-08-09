routes.$inject = ['$stateProvider'];

export default function routes($stateProvider) {
    $stateProvider
        .state('camera', {
            url: '/cameras/:id',
            template: require('./camera.html'),
            controller: 'CameraController',
            controllerAs: 'camera',
            resolve: {
                camera: function ($state, $stateParams, ros) {
                    let result = ros.getCamera($stateParams.id);
                    result.then(function (val) {
                        if ('code' in val) {
                            if (val.code != 200) {
                                $state.go('cameras');
                            }
                        }
                    });
                    return result;
                }
            }
        });
}
