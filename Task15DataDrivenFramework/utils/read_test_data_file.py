import csv
import os.path


class ReadTestDataCSV:
    @staticmethod
    def read_csv_data(file_path='data/testdata.csv'):
        data = []

        try:
            #Open csv file and define the required columns
            with open(file_path, newline='') as file:
                reader = csv.DictReader(file)
                required_columns = {'Username', 'Password', 'Expected_condition'}

                #Verify the required columns are there in csv file
                if not required_columns.issubset(reader.fieldnames):
                    missing_columns = required_columns - set(reader.fieldnames)
                    raise KeyError(f"Missing the following columns in csv file: {missing_columns}")

                #Reading the username, password, and expected condition from each row of the csv
                for row in reader:
                    if any(cell.strip() for cell in row.values()):
                        data.append((row['Username'], row['Password'], row['Expected_condition']))

                if not data:
                    raise ValueError("No valid data found in csv file")

            return data

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Test data file not found in path {file_path} and the error is {e}")

        except Exception as e:
            raise Exception(f"Unexpected error reading CSV: {e}")


