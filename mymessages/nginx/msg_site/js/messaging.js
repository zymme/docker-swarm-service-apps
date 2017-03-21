angular.module('myMessages')
    .controller('MessagingController', function($scope, $http) {

        console.log("Inside the MessagingController ...");

        var messagingList = this;
        messagingList.messageArray = [];

        messagingList.to = null;
        messagingList.msg = null;
        messagingList.title = null;

        messagingList.messages = [{
                text: 'learn AngularJS',
                done: true,
                from: 'Zed',
                to: 'Audra'
            },
            {
                text: 'build an AngularJS app',
                done: false,
                from: 'Audra',
                to: 'Zed'
            }
        ];

        messagingList.getMessages = function() {

            console.log("About to make call to REST API for messages ...");

            $http({
                method: 'GET',
                url: 'http://192.241.227.72:5000/messaging/api/v1.0/messages'
            }).then(function successCallback(response) {
              console.log("success!!");
              var temp = "[" + response.data.messages + "]";
              messagingList.messageArray = JSON.parse(temp);

            }, function errorCallback(response) {
              console.error("ERROR " + response);
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });

        };

        messagingList.getMessages();


        messagingList.addMessage = function() {

          console.log("Entered addMessage() ...");

          var msg_json = {
            "message": {
              "title": messagingList.title,
              "to": messagingList.to,
              "description": messagingList.msg
            }
           }

          var jsondata = JSON.stringify(msg_json);
          console.log(jsondata);

          $http.post("http://192.241.227.72:5000/messaging/api/v1.0/messages", jsondata)
            .then(function(response) {
              console.log("SUCCESS! " + response);

            }, function(err) {
              console.error("ERROR..." + err);

            });

          messagingList.title = '';
          messagingList.msg = '';
          messagingList.to = '';

        };


        messagingList.clearAll = function() {

          console.log("In clearAll() ...");

          $http.delete("http://192.241.227.72:5000/messaging/api/v1.0/messages")
            .then(function(response) {
              console.log("SUCCESS DELETE CALL!");

            }, function(err) {
              console.error("ERROR IN DELETE CALL ..." + err);
            });


        };



    });
