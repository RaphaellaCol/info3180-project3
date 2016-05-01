var app = angular.module("MyApp", ['ui.bootstrap']);


app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{|');
    $interpolateProvider.endSymbol('|}');
  });
  
app.controller("thumbnailCtrl", function($scope, $http, $uibModal){
    $scope.url = "";
    $scope.images = []
    $scope.search = function(){
        var uurl = "/api/thumbnail/process/?url=" + $scope.url;
        $http.get(uurl).success(function(data){
            console.log(data.data.thumbnails);
            $scope.images = data.data.thumbnails;
        });

     };
     
     $scope.open = function (size) {
        $scope.search();
        $scope.animationsEnabled = true;
        var modalInstance = $uibModal.open({
          animation: $scope.animationsEnabled,
          templateUrl: 'myModalContent.html',
          controller: 'ThumbnailCtrl',
          resolve: {
              images: function () {
              return $scope.images;
            }
    
            }
          
        });
        
        modalInstance.result.then(function (img) {
          $scope.img_url = img;
          $scope.selectedimg = img;
        }, function () { 
          
        });
    
    }
    
});


app.controller('ThumbnailCtrl', function ($scope, $http, $uibModalInstance, images) {

  $scope.images = images;

  $scope.selected = "";

  $scope.ok = function () {
    if($scope.selected == ""){
      alert("Please choose an image");
    }else{
  
      $uibModalInstance.close($scope.selected);
    }
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
  
  $scope.dosmn = function(image){
    $scope.selected = image;
  };
});

