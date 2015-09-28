import urllib2
import json
import sys
import csv

key = sys.argv[1]
bus = sys.argv[2]
url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key, bus)

request = urllib2.urlopen(url)
data = json.loads(request.read())

busNumber = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
numberOfBuses = len(busNumber)

with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)

        for i in range(numberOfBuses):
                locationDetails = busNumber[i]["MonitoredVehicleJourney"]["VehicleLocation"]
                tempLongitude = str(locationDetails["Longitude"])
                tempLatitude = str(locationDetails["Latitude"])
                stopDetails = busNumber[i]["MonitoredVehicleJourney"]["OnwardCalls"]
                if stopDetails=={}:
                        stopName="N/A"
                        stopStatus="N/A"
                else:
                        stopName = stopDetails["OnwardCall"][0]["StopPointName"]
                        stopStatus = stopDetails["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
                writer.writerow([tempLatitude, tempLongitude, stopName, stopStatus])
