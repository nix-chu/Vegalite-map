import csv

filelocation = "president_county_candidate.csv"
csv_file = open(filelocation, 'r')
csv_reader = csv.reader(csv_file, delimiter=",")
next(csv_reader, None) # skip header

data = {}
candidates = ["Joe Biden", "Donald Trump"]

for row in csv_reader:
    # row: [state, county, candidate, party, vote, winner]
    if row[2] not in candidates:
        # Skip if irrelevant candidate
        continue

    if row[0] not in data.keys():
        # Add new State into dictionary, then store candidate:votes
        data[row[0]] = { row[2]: int(row[4]) }
    else:
        if row[2] not in data[row[0]].keys():
            # Add new candidate into inner dictionary
            data[row[0]][row[2]] = int(row[4])
        else:
            # Add votes into existing state and candidate
            data[row[0]][row[2]] += int(row[4])

csv_file.close()
f = open("clean_candidate_data.csv", 'w', newline="")
csv_writer = csv.writer(f)
header_row = ["state", "biden_votes", "trump_votes"]
csv_writer.writerow(header_row)

for state in data:
    new_row = [state, data[state]["Joe Biden"], data[state]["Donald Trump"]]
    print(new_row)
    csv_writer.writerow(new_row)

f.close()