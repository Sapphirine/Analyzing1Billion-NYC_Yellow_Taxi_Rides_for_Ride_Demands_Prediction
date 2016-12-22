import csv
import os  

in_file = 'count_all.csv'
count_file = 'final_count_all.txt'
tip_file = 'final_tip_all.txt'
fare_file = 'final_fare_all.txt'

pickup_area_dict = {'Battery_Park_City_Lower_Manhattan': 0,'Chinatown': 1,'Clinton': 2,'East_Village': 3,'Gramercy': 4,
'Hudson_Yards_Chelsea_Flatiron_Union_Square': 5,'Lenox_Hill_Roosevelt_Island': 6,'Lincoln_Square': 7,
'Lower_East_Side': 8,'Midtown_Midtown_South': 9,'Murray_Hill_Kips_Bay': 10,'SoHo_TriBeCa_Civic_Center_Little_Italy': 11,
'Stuyvesant_Town_Cooper_Village': 12,'Turtle_Bay_East_Midtown': 13,'Upper_East_Side_Carnegie_Hill': 14,
'Upper_West_Side': 15,'West_Village': 16,'Yorkville':17}

weather_dict = {'sunny':0, 'rain':1, 'snow':2}

if os.path.isfile(count_file) or os.path.isfile(tip_file) or os.path.isfile(fare_file):
    print "output file exists"
    exit(-1)

with open(in_file,"rb") as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)

    for line in reader:
        area = line[0]
        area_num = pickup_area_dict[area]
        hour = int(line[1])
        is_business = line[2]
        weather = line[3]
        weather_num = weather_dict[weather]
        temp_cat = int(float(line[4]))

        with open(count_file,"ab") as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
            writer.writerow((line[5], '1:'+str(area_num), '2:'+str(hour), '3:'+is_business, '4:'+str(weather_num), '5:'+str(temp_cat)))

        with open(tip_file,"ab") as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
            writer.writerow((line[7], '1:'+str(area_num), '2:'+str(hour), '3:'+is_business, '4:'+str(weather_num), '5:'+str(temp_cat)))

        with open(fare_file,"ab") as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
            writer.writerow((line[6], '1:'+str(area_num), '2:'+str(hour), '3:'+is_business, '4:'+str(weather_num), '5:'+str(temp_cat)))