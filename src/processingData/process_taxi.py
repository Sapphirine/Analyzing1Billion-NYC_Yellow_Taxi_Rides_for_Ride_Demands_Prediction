import csv
import os  
import CalWorkDay
from datetime import date, datetime
import Poly_dict
import testPoly

name = "rmcoled_yellow_tripdata_2016-05.csv"
output = "processed_" + name
weatherFile = 'his_weather.csv'

if os.path.isfile(output):
    print "output file exists"
    exit(-1)


# Get the weather dict
precip_dict = {}
snowfall_dict = {}
temperature_dict = {}
with open(weatherFile,"rb") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader, None)
    for weather_line in reader:
        one_date = datetime.strptime(weather_line[0], '%Y/%m/%d').date()
        precip_dict[str(one_date)] = float(weather_line[1])
        snowfall_dict[str(one_date)] = float(weather_line[2])
        temperature_dict[str(one_date)] = float(weather_line[3])


with open(name,"rb") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader, None)

    # Write header
    header.append('is_business_day')
    header.append('weather')
    header.append('temperature')
    header.append('temperature_cat')
    header.remove('pickup_longitude')
    header[0] = 'pickup_area'
    header[1] = 'pickup_hour'
    
    with open(output,"a") as result:
        writer = csv.writer(result, delimiter=',', lineterminator="\n")
        writer.writerow(header)

    line1 = next(reader)
    date_str = line1[2][0:10]

    date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
    year = date_object.year
    month = date_object.month
    last_day = date_object.day

    first_itr = True

    for line in reader:

        ### Business Day
        off_day_list = CalWorkDay.offDayInMonth(date_object)
        this_date = datetime.strptime(line[2][0:10], '%Y-%m-%d').date()
        day = this_date.day
        if this_date in off_day_list:
            is_business_day = '0'
        else:
            is_business_day = '1'
        line.append(is_business_day)


        ### Time period: divide into hours
        line[2] = line[2][0:13]


        ### Weather & Temperature
        precip = precip_dict[str(this_date)]
        snowfall = snowfall_dict[str(this_date)]
        temperature = temperature_dict[str(this_date)]
        temperature_cat = round(temperature, -1)
        weather = 'sunny'
        if precip > 0.3:
            weather = 'rain'
        if snowfall > 5.0:
            weather = 'snow'


        ### Calculate Polygon
        lng = float(line[0])
        lat = float(line[1])

        for area_name in Poly_dict.Poly_dict:
            poly_list = Poly_dict.Poly_dict[area_name]

            if testPoly.point_in_poly(lat, lng, poly_list) is "IN":

                if area_name[-1] is '1' or area_name[-1] is '2' or area_name[-1] is '3'or area_name[-1] is '4'or area_name[-1] is '5'or area_name[-1] is '6'or area_name[-1] is '7'or area_name[-1] is '8':
                    area_name = area_name[:-2]

                line.insert(0, area_name)
                with open(output,"a") as result:
                    writer = csv.writer(result, delimiter=',', lineterminator="\n")
                    writer.writerow((line[0], line[3], line[4], line[5], line[6], line[7], weather, temperature, temperature_cat))
                break


print "Finished"
exit(0)
