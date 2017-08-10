(function(angular) {

  angular.module('pythosphere', ['ngRoute']);

  var bootstrap = function() {
    angular.element(document).ready(function() {
      angular.bootstrap(document, [ 'pythosphere' ]);
    });
  };

  bootstrap();

}(window.angular));
