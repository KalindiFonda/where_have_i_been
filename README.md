README.md

##### Why?

As part one of the projects of the Front end Nanodegree, we had to do a resume, and so I added a map of the places I've been to. However that did not really work in terms of me keeping it updated - because I'd have to go into the code everytime I am in a new spot, update it by adding coordinates, running it online and so on), so that was way too much, thus I realized that I should do a map with an easy location adding interface, so that I could add places any time.

##### Idea:
Map with markers view page
 	- TODO: info windows
 	- later: maybe some send me suggestions functionality, or add places for me

Input area:
- protected by some auth (maybe google login)
-location:
	- add by name
		- or have self fill location
			(maybe have checkbox to allow this)
			- option to add personal name
		- or check if name is correct
	- add by coordinates
	- click on map

- check on map if location is right
	- would be great: drag and drop precision on map

- notes box

submit ---> puts it into db that feeds page 1.

DB, for now
	- location name
		- city
		- country
	- coordinates
	- TODO: notes


Interesting to look into it in the future:
https://developers.google.com/maps/documentation/javascript/examples/places-autocomplete


##### How to run google app engine?
- go into the google app engine folder (cd /Applications/google_appengine)
- run: python dev_appserver.py /project/folder/path
- to update online: python appcfg.py update /path/to/project