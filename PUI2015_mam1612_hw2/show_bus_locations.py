import urllib2
import json
import sys

key = sys.argv[1]
bus = sys.argv[2]
url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key, bus)

request = urllib2.urlopen(url)
data = json.loads(request.read())

busNumber = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
numberOfBuses = len(busNumber)
print 'The number of active bus connections = ', numberOfBuses

for i in range(numberOfBuses):
    locationDetails = busNumber[i]["MonitoredVehicleJourney"]["VehicleLocation"]
    tempLongitude = str(locationDetails["Longitude"])
    tempLatitude = str(locationDetails["Latitude"])
    print 'Bus '+str(i)+' is at latitude '+tempLongitude+' and longitude '+tempLatitude
