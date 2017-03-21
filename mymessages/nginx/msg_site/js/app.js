
angular.module('myMessages', ['ngRoute'])
  .config(function($routeProvider) {
    console.log("in routeProvider ...");

    $routeProvider
    .when("/", {

      templateUrl : "main.html"
    })
    .when("/messages", {

      templateUrl : "messages.html",
      controller : "MessagingController as msgCtrl"
    })
    .when("/create", {
      templateUrl : "create_message.html",
      controller : "MessagingController as msgCtrl"
    })
    .when("/clearall", {
      templateUrl : "clear_all_messages.html",
      controller : "MessagingController as msgCtrl"
    });

  });
