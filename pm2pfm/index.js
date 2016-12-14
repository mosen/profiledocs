const fs = require('fs');

var casper = require('casper').create({
  verbose: true,
  logLevel: "debug",
  onError: function() {
    this.echo('an error occurred');
  },
  onLoadError: function() {
    this.echo('failed to load something');
  },
  onResourceRequested: function(casper, resource) {
    this.echo('Request (#' + resource.id + '): ' + resource.url);
  }
});

casper.start('index.html', function() {
  this.echo('Loading page from local source');
});

casper.waitForResource("common/app/javascript-packed.js", function() {
  this.echo('Profile Manager packed javascript asset has been loaded');
});

// for (var prop in window.Admin) {
//   if (!window.Admin.hasOwnProperty(prop)) continue;
//   if (!/KnobSet$/.test(prop)) continue;

casper.then(function() {
  this.echo('Scraping Admin.*KnobSet and *KnobSetView');

  var adminExists = this.evaluate(function () {
    return !!window.Admin;
  });

  this.echo(adminExists);

  var payload = this.evaluate(function () {

      var KnobSetClass = window.Admin.IdentificationKnobSet;
      var KnobSetViewClass = window.Admin.IdentificationKnobSetView;


      var payload = {
        // The title displayed on the sidebar in Profile Manager
        'displayName': KnobSetClass.displayName,
        // The valid platforms for this payload, separated by a space
        'platformTypes': KnobSetClass.platformTypes,
        // This name is used as an identifier
        'profilePropertyName': KnobSetClass.profilePropertyName,
        // Payload is valid for System Level
        'systemLevel': KnobSetClass.systemLevel,
        // Payload is valid for User Level
        'userLevel': KnobSetClass.userLevel,
        // List of keys valid for this payload
        'payloadContentKeys': [],
        // Details for each key
        'payloadContent': {}
      };


      // Get mixin values from instantiated versions because that is the only method i can find.
      var knobSet = new KnobSetClass();
      var knobSetView = new KnobSetViewClass();

      var knobSetSuperclass = knobSet.__sc_super__;

      for (var ksProp in knobSetSuperclass) {
        // Search for SC.RecordAttributes which are SproutCore model attrs
        if (knobSetSuperclass.hasOwnProperty(ksProp) && knobSetSuperclass[ksProp] instanceof SC.RecordAttribute) {
          var payloadKey = knobSetSuperclass[ksProp].key;
          payload.payloadContentKeys.push(payloadKey);
          payload.payloadContent[payloadKey] = {};

          payload.payloadContent[payloadKey]["type"] = knobSetSuperclass[ksProp].type.name;
          var defaultValue = knobSetSuperclass[ksProp].defaultValue;
          if (!defaultValue instanceof Object) {
            payload.payloadContent[payloadKey]["defaultValue"] = defaultValue;
          } else {
            payload.payloadContent[payloadKey]["defaultValue"] = JSON.stringify(defaultValue);
          }
        }
      }

      // iterate through view.contentView.childViews
      // look for instances of Admin.KnobSetFieldView
      // the field instance will have __sc_super__ which describes title, description, and fieldContentValueKey
      // some fields dont adhere to this
      // fieldHint might tell you whether this is optional

      return payload;
  });

  this.echo(JSON.stringify(payload));

});

casper.run();
