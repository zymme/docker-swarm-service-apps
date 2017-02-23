
angular.module('myMessages', ['ngRoute'])
  .config(function($routeProvider) {
    $routeProvider
    .when("/", {
      templateUrl : "index.html"
    })
    .when("/messages", {
      templateUrl : "messages.html"
    })
  });
