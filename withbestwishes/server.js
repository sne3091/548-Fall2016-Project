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

        // define model =================
        var Tweet = mongoose.model('Tweet', {
        	text : String
        });
    // routes ======================================================================

    // api ---------------------------------------------------------------------
    // get all todos
    app.post('/api/tweets', function(req, res) { 

    		var options = { screen_name: req.body.text };

    		Twitter.get('friends/list', options , function(err, data) {
    			for (var i = 0; i < data.length ; i++) {
    				console.log(data[i].text);
    			}
    			res.json(data);
    		});
    	});

    // delete a todo
    app.delete('/api/tweet/:tweet_id', function(req, res) {
    	Tweet.remove({
    		_id : req.params.tweet_id
    	}, function(err, todo) {
    		if (err)
    			res.send(err);

            // get and return all the todos after you create another
            Tweet.find(function(err, todos) {
            	if (err)
            		res.send(err)
            	res.json(todos);
            });
        });
    });

    // application -------------------------------------------------------------
    app.get('*', function(req, res) {
        res.sendfile('./public/index.html'); // load the single view file (angular will handle the page changes on the front-end)
    });

    // listen (start app with node server.js) ======================================
    app.listen(8080);
    console.log("App listening on port 8080");
