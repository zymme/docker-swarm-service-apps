
angular.module('myMessages', ['ngRoute'])
  .config(function($routeProvider) {
    console.log("in routeProvider ...");

    $routeProvider
    .when("/", {

      templateUrl : "main.html"
    })
    .when("/messages", {

      templateUrl : "messages.html"
      // controller : "MessagingController"
    })
    .when("/create", {
      templateUrl : "create_message.html"
    });
    
  });
