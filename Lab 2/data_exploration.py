import pandas as pd
import pdfplumber
import requests


def get_raw_data_from_url(url,file_name):
    response = requests.get(url)
    file_name = "Lab 2\\raw_data\\" + file_name

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully as {file_name}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        
def extract_text_from_pdf(pdf_file,text_file_name):
    extracted_text = ""
    with pdfplumber.open("Lab 2\\raw_data\\"+pdf_file) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text()

    text_file = "Lab 2\\raw_data\\" + text_file_name
    with open(text_file, "w", encoding="utf-8") as file:
        file.write(extracted_text)
    print(f"Text extracted and saved to {text_file}")
    
def get_data_from_text(text_file):
    text_file = "Lab 2\\raw_data\\" + text_file
    
    with open(text_file, "r", encoding="utf-8") as file:
        extracted_text = file.read()
    data = []
    columns = ["Day", "Time", "Activity"]  
    current_day = None

    for line in extracted_text.split("\n"):
        line = line.strip()
        if line.isupper() and "DAY" in line:  
            current_day = line
        elif current_day and ":" in line:  
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                time, activity = parts
                data.append([current_day, time, activity])
    if data:
        df = pd.DataFrame(data, columns=columns)
        return df
    else:
        print("No structured data found in the extracted text.")
        return None

def save_to_csv(df, csv_file):
    df.to_csv(csv_file, index=False)
    print(f"Data saved to CSV file: {csv_file}")
    
    

if __name__ == "__main__":
    # Define the PDF file name and URL
    pdf_file = "LA_Tourist_Itinerary.pdf"
    url = "https://latourist.com/documents/LA_Tourist_Itinerary.pdf"

    # Download the raw PDF file from the URL
    get_raw_data_from_url(url, pdf_file)

    # Extract text from the downloaded PDF file and save it to a text file
    extract_text_from_pdf(pdf_file, "LA_Tourist_Itinerary.txt")

    # Extract structured data from the text file and create a DataFrame
    df = get_data_from_text("LA_Tourist_Itinerary.txt")

    # Save the DataFrame to a CSV file
    save_to_csv(df, "Lab 2\\processed_data\\LA_Tourist_Itinerary.csv")

    # Print the first few records of the DataFrame
    print("\nFirst few records:")
    print(df.head())

    # Print the dimensions of the DataFrame
    print("\nDataset dimensions:")
    print(df.shape)

    # Check for missing data in the DataFrame
    print("\nMissing data check:")
    print(df.isnull().sum())
