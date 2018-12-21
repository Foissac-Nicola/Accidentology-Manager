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
    hidden: true,
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

       //document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
        navigator.geolocation.getCurrentPosition(this.onSuccess, this.onError,{timeout:1000,enableHighAccuracy: false});
        document.getElementById("searchButton").onclick = function(){
            if(app.hidden){
                app.removeDisplayInstructions(false);
                app.control.show();
                document.getElementsByClassName("leaflet-routing-container leaflet-bar leaflet-routing-collapsible leaflet-control")[0].setAttribute('style', 'width : 360px; height : 515px;');
                app.hidden = false;
            }
            else{
                app.control.hide();

                 document.getElementsByClassName("leaflet-routing-container leaflet-bar leaflet-routing-collapsible leaflet-control")[0].setAttribute('style', 'width : 0px; height : 0px;');

                app.hidden = true;
            }
                  /*  document.getElementById("mapDisplay").setAttribute('style', 'display:none;');
                    document.getElementById("searchForm").setAttribute('style', 'display:block;');*/
        }
    },


    displayInstrutions: function(domElement){
        document.getElementsByClassName("routesToDisplay")[0].setAttribute('style', 'display : none');

        var d = domElement.parentNode.parentNode;

        document.getElementsByClassName("instructionToDisplay")[0].setAttribute("style","height:500px;");
        document.getElementsByClassName("instructionToDisplay")[0].appendChild(d.cloneNode(true));
        document.getElementsByClassName("instructionToDisplay")[0].getElementsByTagName("h3")[0].innerHTML= document.getElementsByClassName("instructionToDisplay")[0].getElementsByTagName("h3")[0].innerHTML.split("<button")[0]+"<button onclick='app.removeDisplayInstructions(true)'>&#10060;</button></h3>";
        document.getElementsByClassName("instructionToDisplay")[0].getElementsByTagName("table")[0].setAttribute("style","display:block; height:400px;overflow:auto;");

        document.getElementsByClassName("instructionToDisplay")[0].appendChild(document.getElementsByClassName("instructionToDisplay")[0].getElementsByTagName("table")[0]);



    },

    removeDisplayInstructions: function(displayChoices){
        var instructions = document.getElementsByClassName("instructionToDisplay")[0];

        while (instructions.firstChild) {
            instructions.removeChild(instructions.firstChild);
        }

        if(displayChoices){
            document.getElementsByClassName("routesToDisplay")[0].setAttribute('style', 'display : block');
        }

    },

    onSuccess: function(position){
        app.userLocation = [position.coords.latitude,position.coords.longitude];
        console.log("Location retreived successfully");
        app.startMap();
    },

    onError: function(error){
            console.log('code: '    + error.code    + '\n' +
          'message: ' + error.message + '\n');
            console.log("assuming coordinates are La Rochelle");
            app.userLocation = [46.162,-1.2463];
            app.startMap();
    },

    // deviceready Event Handler
    //
    // Bind any cordova events here. Common events are:
    // 'pause', 'resume', etc.
   /* onDeviceReady: function() {
        this.receivedEvent('deviceready');
    },*/

    // Update DOM on a Received Event
   /* receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    },*/


    startMap: function(){
        this.mymap = L.map('mapid').setView(this.userLocation, 10);

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

        this.control.addTo(this.mymap);

        this.hidden = true;



        var info = L.control({position: 'bottomright'});

        info.onAdd = function (map) {
            this._div = L.DomUtil.create('div', 'routesToDisplay'); // create a div with a class "info"
            return this._div;
        };

        info.addTo(this.mymap);


        var instructions = L.control({position: 'bottomleft'});

        instructions.onAdd = function (map) {
            this._div = L.DomUtil.create('div', 'instructionToDisplay'); // create a div with a class "info"
            L.DomEvent.disableClickPropagation(this._div);
            return this._div;
        };

        instructions.addTo(this.mymap);

        // Disable dragging when user's cursor enters the element
        instructions.getContainer().addEventListener('mouseover', function () {
            app.mymap.dragging.disable();
        });

        // Re-enable dragging when user's cursor leaves the element
        instructions.getContainer().addEventListener('mouseout', function () {
            app.mymap.dragging.enable();
        });
            /*var html = this.control.getContainer().getElementsByClassName("leaflet-routing-geocoders");


            if(html !== "undefined" && html !== null){
                if(html[0] !== "undefined" && html[0] !== null){
                    var routesMenu = document.getElementById("searchForm");
                    routesMenu.appendChild(html[0]);
                }
            }*/


        document.getElementsByClassName("routesToDisplay")[0].appendChild(this.control.getContainer().getElementsByClassName("leaflet-routing-alternatives-container")[0]);

        var d = document.createElement("div");
        d.id= "messages";
        d.innerHTML = '<h3>Veuillez sélectionner une destination</h3>';


        var l = document.createElement("div");
        l.id= "loading";
        l.innerHTML = '<img src="images/loading.gif" height="64" width="64">';

        l.setAttribute("style", "display:none");


        document.getElementsByClassName("routesToDisplay")[0].appendChild(d);
        document.getElementsByClassName("routesToDisplay")[0].appendChild(l);


        var b = document.createElement('button');
        b.setAttribute('content', 'test content');
        b.setAttribute('class', 'btn');
        b.setAttribute("style","left:135px;position: absolute; bottom: 30px;");


        b.onclick = function (event) {
            if(app.control.getPlan().isReady())
            {
                app.control.route();
            }
            else{
                alert("Un des points de passage est introuvable/erroné, veuillez corriger et réessayer.");
            }
        };
        b.innerHTML = 'Rechercher';

        document.getElementsByClassName("leaflet-routing-container leaflet-bar leaflet-routing-collapsible leaflet-control")[0].appendChild(b);
        this.control.hide();


    }

};

app.initialize();