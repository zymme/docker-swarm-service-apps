angular.module('myMessages')
    .controller('MessagingController', function($scope, $http) {

        console.log("Inside the MessagingController ...");

        var messagingList = this;
        messagingList.messageArray = [];

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
                url: 'http://localhost:5000/messaging/api/v1.0/messages'
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

          console.log("inside addMessage function() ...");

            // messagingList.messages.push({
            //     from: 'Me',
            //     to: 'You',
            //     text: messagingList.msgText,
            //     done: false
            // });
            messagingList.msgText = '';

        };



    });
