// server.js

    // set up ========================
    var express  = require('express');
    var TwitterPackage = require('twit');
    var app      = express();                               // create our app w/ express
    var mongoose = require('mongoose');                     // mongoose for mongodb
    var morgan = require('morgan');             // log requests to the console (express4)
    var bodyParser = require('body-parser');    // pull information from HTML POST (express4)
    var methodOverride = require('method-override'); // simulate DELETE and PUT (express4)

    // configuration =================

    mongoose.connect('mongodb://localhost:27017/db');     // connect to mongoDB database on modulus.io

    app.use(express.static(__dirname + '/public'));                 // set the static files location /public/img will be /img for users
    app.use(morgan('dev'));                                         // log every request to the console
    app.use(bodyParser.urlencoded({'extended':'true'}));            // parse application/x-www-form-urlencoded
    app.use(bodyParser.json());                                     // parse application/json
    app.use(bodyParser.json({ type: 'application/vnd.api+json' })); // parse application/vnd.api+json as json
    app.use(methodOverride());
    var secret = {
    	consumer_key: '3iORjTEMdSsBT6imASv3Q93or',
    	consumer_secret: 'cT6scj9F2D1aZnmcvE6uYP0HpVrSTcZSJfokAODGvemeHbGJft',
    	access_token: '113674445-p0dVzfOYFgYEkUyaKNZ7fXvZ3XzXEizB1UYF5x42',
    	access_token_secret: 'WNFyCEG5HKqpWcJkPGpLjXb7TfwpwU7Lo20qf0SNAv2UA'
    }
    var Twitter = new TwitterPackage(secret);

    var schema = new mongoose.Schema({ _id: mongoose.Schema.Types.ObjectId, url: String, title: String, rating: String, price_min: Number, price_max: Number,
    image: String, category: String });
    // define model =================
    var Gifts = mongoose.model('Gifts', schema);
    // routes ======================================================================

    // api ---------------------------------------------------------------------
    // get all todos
    var domain_nba = ['LA Lakers','New York Knicks','Chicago Bulls','Golden State Warriors','San Antonio Spurs','Michael Jordan',
    'Stephen Curry','Kobe Bryant','Joakim Noah','Tim Duncan'];
    var domain_nfl = ['New England Patriots','Seattle Seahawks','Carolina Panthers','Dallas Cowboys','Denver Broncos','Tom Brady',
    'Cam Newton','Russell Wilson','Dak Prescott','Peyton Manning'];
    var domain_soccer = ["Manchester United","FC Barcelona","Arsenal","Real Madrid","Chelsea","Wayne Rooney","Lionel Messi","Mesut Ozil",
    "Cristiano Ronaldo","Neymar"];
    var domain_ncaa = ['USC Trojans',"Ohio State Buckeyes","Alabama Football","Washington Athletics","UCLA Athletics"];
    var domain_bb = ["Chicago Cubs","Los Angeles Dodgers","New York Yankees","San Francisco Giants","Boston Red Sox","Kris Bryant","Clayton Kershaw",
    "Gary Sanchez","Dustin Pedroia","Madison Bumgarner"];
    var domain_hockey = ["Columbus Blue Jackets","Pittsburgh Penguins","New York Rangers","Philadelphia Flyers","Carolina Hurricanes"];
    var domain_tennis = ["Rafael Nadal","Roger Federer","Serena Williams","Maria Sharapova","Novak Djokovic"];

    function getGiftsQuery(category, price_min, price_max){
        var query = Gifts.find({category:{ $in:category }, price_min:{ $gte: price_min }, price_max: { $lte: price_max }});
        return query;
    }

    app.post('/api/getItems', function(req, res) { 
            var search_by = req.body.searchby;
    		var options = { screen_name: req.body.text, count: 200 };
            var budget = req.body.budget;
            var price_arr = budget.split("-");
            var price_min=parseInt(price_arr[0].substring(1));
            var price_max=parseInt(price_arr[1].substring(1));
            if(search_by=='twitter'){
        		Twitter.get('friends/list', options , function(err, data) {
                    var interest = [];
                    for (var i = data.users.length - 1; i >= 0; i--) {
                        if(domain_nba.indexOf(data.users[i].name) > -1 || domain_nfl.indexOf(data.users[i].name) > -1 ||
                         domain_soccer.indexOf(data.users[i].name) > -1 || domain_ncaa.indexOf(data.users[i].name) > -1 || 
                         domain_bb.indexOf(data.users[i].name) > -1 || domain_hockey.indexOf(data.users[i].name) > -1 || 
                         domain_tennis.indexOf(data.users[i].name) > -1 ){
                            interest.push(data.users[i].name);    
                        }
                    }
                    var query = getGiftsQuery(interest, price_min, price_max);
                    query.exec(function(err,items){
                        if(err)
                          return console.log(err);
                        res.json(items);
                    });
        		});
            }else{
                var input = req.body.text.split(",");
                var interest = []
                for (var i = input.length - 1; i >= 0; i--){
                    interest.push(input[i]); 
                }
                var query = getGiftsQuery(interest, price_min, price_max);
                query.exec(function(err,items){
                    if(err)
                      return console.log(err);
                    res.json(items);
                });
            }
    	});


    // application -------------------------------------------------------------
    app.get('*', function(req, res) {
        res.sendfile('./public/index.html'); // load the single view file (angular will handle the page changes on the front-end)
    });

    // listen (start app with node server.js) ======================================
    app.listen(8080);
    console.log("App listening on port 8080");
