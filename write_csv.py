import csv


def write_csv(file, header, data):

    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    return
