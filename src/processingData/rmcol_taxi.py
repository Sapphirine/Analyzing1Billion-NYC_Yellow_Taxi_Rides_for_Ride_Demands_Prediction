import csv
import os  

input_file = "yellow_tripdata_2015-12.csv"
output = "rmcoled_" + input_file

if os.path.isfile(output):
    print "output file exists"
    exit(-1)

with open(input_file,"rb") as source:
    rdr= csv.reader( source )

    with open(output,"wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[5], r[6], r[1], r[4], r[12], r[15]) )

print "Finished"
exit(0)
