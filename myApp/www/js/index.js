/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
var app = {

    mymap: null,
    control: null,
    good_style: [{color: 'black', opacity: 0.15, weight: 9},
                {color: 'white', opacity: 0.8, weight: 6},
                {color: 'green', opacity: 1, weight: 2}],

    mild_style: [{color: 'black', opacity: 0.15, weight: 9},
                {color: 'white', opacity: 0.8, weight: 6},
                {color: 'yellow', opacity: 1, weight: 2}],

    bad_style: [{color: 'black', opacity: 0.15, weight: 9},
                {color: 'white', opacity: 0.8, weight: 6},
                {color: 'red', opacity: 1, weight: 2}],
    // Application Constructor
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },

    // deviceready Event Handler
    //
    // Bind any cordova events here. Common events are:
    // 'pause', 'resume', etc.
    onDeviceReady: function() {
        this.receivedEvent('deviceready');
    },

    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    },


    startMap: function(){
        this.mymap = L.map('mapid').setView([51.505, -0.09], 13);

        L.tileLayer.here({appId: 'MfEihsDsmlJT96yodOUl', appCode: 'd6ZS0xmcVvTCiC6SkWzqew'}).addTo(this.mymap);

        this.control = L.Routing.control({
            waypoints: [],
            altLineOptions: {styles : this.good_style},
            showAlternatives : true,
            router : new L.Routing.Here("MfEihsDsmlJT96yodOUl","d6ZS0xmcVvTCiC6SkWzqew", {alternatives : 2}),
            routeWhileDragging: false,
            geocoder: L.Control.Geocoder.here({app_id :"MfEihsDsmlJT96yodOUl" ,app_code :"d6ZS0xmcVvTCiC6SkWzqew"}),
        });

        this.control.on('routeselected', function(e) {
        var route = e.route;
    });

        console.log(this.control);
        this.control.addTo(this.mymap);

    }

};

app.initialize();
app.startMap();