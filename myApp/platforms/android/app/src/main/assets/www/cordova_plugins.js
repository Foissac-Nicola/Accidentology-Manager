cordova.define('cordova/plugin_list', function(require, exports, module) {
module.exports = [
  {
    "id": "cordova-plugin-geolocation.geolocation",
    "file": "plugins/cordova-plugin-geolocation/www/android/geolocation.js",
    "pluginId": "cordova-plugin-geolocation",
    "clobbers": [
      "navigator.geolocation"
    ]
  },
  {
    "id": "cordova-plugin-geolocation.PositionError",
    "file": "plugins/cordova-plugin-geolocation/www/PositionError.js",
    "pluginId": "cordova-plugin-geolocation",
    "runs": true
  },
  {
    "id": "cordova-plugin-locationservices.Coordinates",
    "file": "plugins/cordova-plugin-locationservices/www/Coordinates.js",
    "pluginId": "cordova-plugin-locationservices",
    "clobbers": [
      "cordova.plugins.locationServices.Coordinates",
      "plugin.locationServices.Coordinates"
    ]
  },
  {
    "id": "cordova-plugin-locationservices.PositionError",
    "file": "plugins/cordova-plugin-locationservices/www/PositionError.js",
    "pluginId": "cordova-plugin-locationservices",
    "clobbers": [
      "cordova.plugins.locationServices.PositionError",
      "plugin.locationServices.PositionError"
    ]
  },
  {
    "id": "cordova-plugin-locationservices.Position",
    "file": "plugins/cordova-plugin-locationservices/www/Position.js",
    "pluginId": "cordova-plugin-locationservices",
    "clobbers": [
      "cordova.plugins.locationServices.PositionError",
      "plugin.locationServices.PositionError"
    ]
  },
  {
    "id": "cordova-plugin-locationservices.LocationServices",
    "file": "plugins/cordova-plugin-locationservices/www/LocationServices.js",
    "pluginId": "cordova-plugin-locationservices",
    "clobbers": [
      "cordova.plugins.locationServices.geolocation",
      "plugin.locationServices.geolocation"
    ]
  },
  {
    "id": "cordova-plugin-splashscreen.SplashScreen",
    "file": "plugins/cordova-plugin-splashscreen/www/splashscreen.js",
    "pluginId": "cordova-plugin-splashscreen",
    "clobbers": [
      "navigator.splashscreen"
    ]
  }
];
module.exports.metadata = 
// TOP OF METADATA
{
  "cordova-plugin-whitelist": "1.3.3",
  "cordova-plugin-geolocation": "4.0.1",
  "cordova-plugin-locationservices": "2.1.0",
  "cordova-plugin-splashscreen": "5.0.2"
};
// BOTTOM OF METADATA
});