import requests
import csv

def write_to_csv(data, file_format):
    if file_format == 'prescription':
        csv_filename = 'prescription_data.csv'
    elif file_format == 'patient_details':
        csv_filename = 'patient_details_data.csv'
    else:
        raise ValueError(f"Invalid file_format: {file_format}")

    try:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(data)

        print(f"Data written to {csv_filename} successfully!")

    except Exception as e:
        print(f"Error writing to CSV file: {str(e)}")


def submit_data(file_format):
    # Replace with the appropriate URL where your FastAPI server is running
    api_url = 'http://127.0.0.1:8000/extract_from_doc'

    # Example data to send, replace with your actual data handling logic
    data = {
        'file_format': file_format,
        # Add more fields as needed based on your application logic
    }

    try:
        # Make a POST request to trigger the extraction
        response = requests.post(api_url, files={'file': open('path_to_your_file', 'rb')}, data=data)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        extracted_data = response.json()  # Assuming the response contains JSON data

        # Write extracted data to CSV
        write_to_csv(extracted_data, file_format)

    except requests.exceptions.RequestException as e:
        print(f"Error making request to API: {str(e)}")
    except Exception as e:
        print(f"Error processing data: {str(e)}")

if __name__ == '__main__':
    file_format = 'prescription'  # Replace with 'patient_details' for patient details data
    submit_data(file_format)
