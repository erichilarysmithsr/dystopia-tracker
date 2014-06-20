
var TimelineCtrl = function($scope, Prediction, Categories, Sources, $rootScope, $location, $filter, $cookies, $timeout, FiltersReset) {
    $scope.filters = { page_size : 200 };
    angular.extend(this, new HomeCtrl($scope, Prediction, Categories, Sources, $rootScope, $location, $filter, $cookies, $timeout, FiltersReset));

    $scope.changeLanguage = function(lang) {
        $scope._lang = $scope.language = lang;
        $location.path('/' + $scope.language + '/timeline');
        $scope.translateTo($scope.language);
        $scope.update(false);
    };

    $scope.spinner = true;

    $scope.$watch(function() { return $scope.predictions }, function() {
        if ($scope.predictions.length && !$scope.hideMoreButton) {
            $scope.spinner = true;
            $scope.update(false);
        } else {
            $scope.spinner = false;
        }
    }, true);
};

angular.module('dystopia-tracker').controller('TimelineCtrl', ['$scope', 'Prediction', 'Categories', 'Sources', '$rootScope', '$location', '$filter', '$cookies', '$timeout', 'Filters', TimelineCtrl]);

// it's the end of the code as we know it