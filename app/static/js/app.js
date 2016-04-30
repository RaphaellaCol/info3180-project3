
<div ng-app="myApp" ng-controller="thumbnailCtrl">
<li ng-repeat="x in thumbnails">{{x.thumbnails}}</li>
</div>

var app = angular.module("MyApp", []);

app.controller("thumbnailCtrl", function($scope, $http){
    $scope.url = ""
    $scope.search = function(){
        var uurl = "/api/thumbnail/process?" + $scope.url;
        $http.get(uurl).success(function(data){
            console.log(data.data.thumbnails);
        })

     }
    
});


