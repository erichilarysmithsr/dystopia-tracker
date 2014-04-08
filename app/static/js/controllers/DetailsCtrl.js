angular.module('dystopia-tracker').controller('DetailsCtrl', ['$scope', 'Prediction', 'Categories', 'Sources', '$rootScope', '$location', '$routeParams', '$cookies',
                                                           function($scope, Prediction, Categories, Sources, $rootScope, $location, $routeParams, $cookies) {
    
    
    // check if user has visited the site before
    if ($cookies.alreadyVisited) {
        $scope.returningVisitor = true;
    };
    // set cookie
    $cookies.alreadyVisited = 'true';
    $scope.prediction = [];
    $scope.realisations = [];
    $scope.category = [];
    $scope.shareurls = [];
    $scope.more = [];
    $scope.filters = {exclude : $routeParams.id, title : '', author : '', category : ''};
    $scope.language = $rootScope._lang;
    /* create array to story year_published of source, year_predicted of prediction, and year_introduced of all realisations
    including the corresponding descriptions */
    $scope.alldates = [];
    $scope.sorting = 'year';
    $scope.isTranslating = false;
    
    Prediction.get({id:$routeParams.id}).success(function(data) {
		$scope.prediction = data;
		$scope.prediction.amzn = "http://www.amazon.de/s/?url=search-alias=aps&field-keywords=" + data.source.title + "&tag=davidbauerch-21&link_code=wql&_encoding=UTF-8";
        $scope.realisations = _.filter($scope.prediction.realisations, function(elem) {
            return elem['description_' + $scope._lang];
        });
		createYearsArray($scope.prediction,$scope.realisations);
	    getCategoryTitle($scope.prediction.category);
		getMore("title",$scope.prediction.source.title);
        getMore("author",$scope.prediction.source.author);
        getMore("category",$scope.prediction.category);
    });	
    
    function getCategoryTitle(id) {
        Categories.get({id:id}, function(data) {
        $scope.category = data;
        });
    };
   
    function createYearsArray(prediction,realisations) {
        // push all year values into the array
        $scope.alldates.push({"year":prediction.source.year_published, "text": "", "img":prediction.source.image, "credit": "", "type": "published", "link": prediction.source.more_info, "amzn": prediction.amzn});
        
        if (prediction.year_predicted != 0) {
            $scope.alldates.push({"year":prediction.year_predicted, "text": "", "img":"", "credit": "", "type":"predicted","link": prediction.more_info});
        }
        
        for (var i=0;i<realisations.length;i++) {
    	    $scope.alldates.push({"year":realisations[i].year_introduced, "text": realisations[i].description_E, "img":realisations[i].image, "credit": realisations[i].username, "type":"introduced", "link": realisations[i].more_info});    
        };
    };
    
      
    function getMore(param,value) {
        filters = {exclude : $routeParams.id} 
        filters[param] = value;
        console.log(filters);
	    Prediction.get(filters).success(function(data) {
		    $scope.more[param] = data.results;
		    console.log(data.results);
	    });    
    }
    
    // TODO: add text and images to optimise sharing: http://ar.zu.my/how-to-really-customize-the-deprecated-facebook-sharer-dot-php/
    $scope.shareurls.fb = "http://www.facebook.com/sharer.php?u=" + $location.absUrl();
    $scope.shareurls.twi = "http://twitter.com/share?url=" + $location.absUrl();
    $scope.shareurls.mail = "mailto:?Subject=Dystopia Tracker&Body=" + $location.absUrl();
    
    // translation
    $scope.translate = function() {
	   
	    
	    Prediction.post($scope.prediction).success(function(data) {



		    });
    };
    
    
}]); // it's the end of the code as we know it
