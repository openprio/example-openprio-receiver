# Example OpenPrio Receiver

This is an example project how to retrieve openprio data from the NDOVLoket. Openprio contains every second location updates of public transport. That is a much higher frequency of updates than currently provided by KV6. This realtime dataset can open up a world of new opportunities, for example a flighradar24 for public transport, the realtime position of the upcoming busses plotted on a map on passenger information systems, bottle neck analysis or moving some onboard computer functionality to the cloud that could accelerate inovation and reduce costs of development. And probably many more opportunities. 

## iVRI
The initial goal of this datastream was to do a pilot with priority for public transport on the N207 with iVRI's https://www.youtube.com/watch?v=GGPAv_PSnGo. Currently all blue Arriva Qliner buses in Zuid-Holland are in this datafeed. It is unknown for how long this experimental feed will be available. 

## Install
To use this script you have to install python3 and run:
```pip install -r requirements.txt```

You can start the script with:
```python3 main.py```