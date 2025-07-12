import csv
import os.path
from datetime import datetime


class WriteInTestDataCSV:
    # Class variable to auto generate test id
    test_id_generator = 0

    @classmethod
    def get_test_id(cls):
        cls.test_id_generator += 1
        return f"TC_{cls.test_id_generator:03d}"  # Returns test case id in TC_001, TC_002 format

    @staticmethod
    def write_test_result(username, password, expected_condition, test_status):
        # File path
        file_path = "data/testdata.csv"
        file_exists = os.path.exists(file_path)

        # Define the column headers
        headers = ["Test_ID", "Username", "Password", "Expected_condition", "Date", "Time_of_test", "Name_of_tester",
                   "Test_status"]

        # Prepare new row data
        date = datetime.now().strftime('%Y-%m-%d')
        time_of_test = datetime.now().strftime('%H:%M:%S')
        tester_name = 'Indu'

        # Read existing data if file exists
        rows = []
        if file_exists:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                existing_headers = next(reader, None)  # Read headers
                rows = list(reader)  # Read all rows

            found = False
            for i, row in enumerate(rows):
                if len(row) >= 3 and row[1] == username and row[2] == password:  # Check username and password
                    rows[i] = [WriteInTestDataCSV.get_test_id(), username, password, expected_condition, date,
                               time_of_test, tester_name, test_status]
                    found = True
                    break

            if not found:
                # If no match, create new row with new test_id
             rows.append(
                    [WriteInTestDataCSV.get_test_id(), username, password, expected_condition, date, time_of_test,
                    tester_name, test_status])


        # Write all data back to file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write headers
            writer.writerow(headers)
            # Write all rows
            writer.writerows(rows)
