# visual music
Project for CalHacks 3.0
by Erik Dyer, Jiayin Tang

visualizes music using sentiment analysis of lyrics

best experience in Chrome

try songs with varying sentiments.
we used: 9 by Drake; I'll Be Alright by Passion Pit; Lost by Temper Trap

## to run
```
python services.py
python manage.py runserver
```

## dependencies/sources
1. MusixMatch API - register and get unique API key
2. IBM Watson Alchemy API - register and get unique API key; install [SDK](https://github.com/watson-developer-cloud/python-sdk); also requires Python >2.7.8
3. [Preziotte's Party Mode](https://github.com/preziotte/party-mode) - relied on heavily for visualization of music


### features that would be nice to have
1. search option for songs
2. have sentiment analysis and color change working for files that the user drags and drops into the window
3. have colors change for all themes

