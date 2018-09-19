export default function routes($stateProvider) {
    $stateProvider
        .state('filters', {
            url: '/filters',
            template: require('./filters.html'),
            controller: 'FiltersController',
            controllerAs: 'filters',
            resolve: {
                camerasResolved: function (CamerasService) {
                    return CamerasService.getCamerasList();
                },
                filterTypesResolved: function (FiltersService) {
                    return FiltersService.getFilterTypes();
                }
            }
        });
}

routes.$inject = ['$stateProvider'];
