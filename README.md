# Features
The script is designed for various data manipulation tasks using the Pandas library, including CSV file handling, data filtering and merging, arithmetic operations, and fetching data from web APIs.
## CSV File Handling
- **Reading CSV**: Reads a CSV file from a specified path.
- **Writing CSV**: Writes data to a CSV file with a naming format that includes the current date.

## Data Manipulation Functions
- **select_item**: Filters rows based on specified conditions in given columns.
- **add_data**: Concatenates two data frames vertically.
- **subtract**: Performs subtraction between two columns in a data frame.
- **sum_all_data**: Calculates the sum of all data across specified columns.
- **combine_data_with_time**: Merges multiple columns with a 'time' column based on a specified condition.
- **split_data**: Splits data based on conditions and renames columns accordingly.
- **replace_name**: Replaces values in a specified column based on a given dictionary of replacement rules.

## Data Renaming
- **Rename Header**: Renames dataframe columns.
- **Rename Values in Header**: Changes specific values in a data frame column.

## Utility
- **fetch_data_wb**: Fetches data from a web API using the requests library.

## Usage
- **CSV File Handling**: Update file paths and column names as per your data schema.
- **Data Manipulation Functions**: Customize the functions according to your dataset and requirements.
- **Data Renaming**: Modify the renaming rules for your data.
- **fetch_data_wb**: Set the URL, params, and other request details as per the API you are using.

## Requirements
- Python 3.x
- Pandas
- Requests (for web API fetching)

**Note**: Ensure that the paths, URLs, column names, and other specific values are updated to match your specific use case and data schema. The script is a template and may require modifications for different datasets and requirements.
