#!/bin/bash
terser --source-map -o js/mcstats.min.js js/dev/mcstats.js js/dev/mcstats-widgets.js js/dev/mcstats-awardlist.js js/dev/mcstats-awardview.js js/dev/mcstats-eventlist.js js/dev/mcstats-eventview.js js/dev/mcstats-playerlist.js js/dev/mcstats-playerview.js js/dev/mcstats-hof.js js/dev/mcstats-loader.js js/dev/mcstats-start.js
uglifycss style.css > style.min.css