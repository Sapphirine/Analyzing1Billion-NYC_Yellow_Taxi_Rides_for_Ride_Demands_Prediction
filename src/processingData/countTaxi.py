import csv
import os  
import json

in_file_list = []
output = "count_taxi_tripdata.csv"

#if os.path.isfile(output):
#    print "output file exists"
#    exit(-1)

print "*** Initializing all_dict ***"

all_dict = {}

for in_file in in_file_list:
    print "Reading " + in_file
    with open(in_file,"rb") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)
        try:
            for line in reader:
                location = line[0]
                hour = line[1][11:13]
                is_business_day = line[5]
                weather = line[6]
                temp_cat = line[8]

                all_key = location + ';' + hour + ';' + is_business_day + ';' + weather + ';' + temp_cat
                all_dict[all_key] = [0, 0.0, 0.0, []]
        except csv.Error:
            pass


print "*** Filling all_dict ***"

for in_file in in_file_list:
    print "Reading " + in_file
    with open(in_file,"rb") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)
        try:
            for line in reader:
                location = line[0]
                hour = line[1][11:13]
                is_business_day = line[5]
                weather = line[6]
                temp_cat = line[8]

                date = line[1][0:10]

                all_key = location + ';' + hour + ';' + is_business_day + ';' + weather + ';' + temp_cat
                all_dict[all_key][0] += 1
                all_dict[all_key][1] += float(line[3])
                all_dict[all_key][2] += float(line[4])
                if date not in all_dict[all_key][3]:
                    all_dict[all_key][3].append(date)
        except csv.Error:
            pass


print "*** Writing output ***"

json.dump(all_dict, open("all_dict.txt",'wb'))


with open(output,"wb") as csvfile:
    writer = csv.writer(csvfile, delimiter=',', lineterminator="\n")
    header = ['area','hour','is_business_day','weather','temp_cat','trip_count','avg_fare','avg_tips', 'total_day_count','num_of_days']

    for key in all_dict:
        key_split = key.split(';')
        total_day_count = all_dict[key][0]
        num_of_days = len(all_dict[key][3])
        avg_count = float(total_day_count) / num_of_days
        avg_fare = round(all_dict[key][1] / total_day_count, 3)
        avg_tips = round(all_dict[key][2] / total_day_count, 3)

        writer.writerow((key_split[0], key_split[1], key_split[2], key_split[3], key_split[4], avg_count, avg_fare, avg_tips, total_day_count, num_of_days))