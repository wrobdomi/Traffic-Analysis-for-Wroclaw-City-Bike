import csv

table_name = 'stacje_projektowe'
geom_field = 'stacja_geom'
nazwa_field = 'stacja_nazwa'
filename = 'input_stations_extended.csv'

def stations_to_sql_inserts():
    inserts = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            temp = 'INSERT INTO ' + table_name + ' (' + geom_field + ',' + nazwa_field + ') VALUES ' + '(ST_GeomFromText' \
                "('POINT(" + str(float(line[1])) + ' ' + str(float(line[2])) + ")'" + ',4326), ' + "'" + line[3] + "');"
            print(temp)

stations_to_sql_inserts()