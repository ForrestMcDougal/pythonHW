import csv
import os

from us_state_abbrev import us_state_abbrev

# read in data
filename = os.path.join('raw_data', 'employee_data.csv')
with open(filename, newline='') as csvfile:
    csv_data = csv.reader(csvfile)
    data = [row for row in csv_data]

filename = os.path.join('assets', 'employee_data_cleaned.csv')
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN',
                        'State'])
    for i in range(1, len(data)):
        # employee id does not change
        emp_id = data[i][0]

        # name is split into two columns
        f_name = data[i][1].split(' ')[0]
        l_name = data[i][1].split(' ')[1]

        # split date of birth into three values for month, day, and year
        dob_year = data[i][2].split('-')[0]
        dob_month = data[i][2].split('-')[1]
        dob_day = data[i][2].split('-')[2]

        # only save last four digits of SSN
        ssn = data[i][3].split('-')[2]

        # use dictionary to lookup state abbreviation
        state = us_state_abbrev[data[i][4]]

        # write data to file
        csvwriter.writerow([emp_id, f_name, l_name,
                            f'{dob_month}/{dob_day}/{dob_year}',
                            f'***-**-{ssn}', state])
