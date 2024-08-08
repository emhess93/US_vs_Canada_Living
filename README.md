# Where to live - US or Canada?

## Overview

My capstone project for CODE:You involves analyzing data to decide where my significant other and I may want to settle. Some factors for consideration include distance to family, monthly expenses, and lifestyle costs. The goal of the project is to demonstrate a general knowledge of Python/pandas, utilization of API's, and data visualization via myplot/seaborn.

## Data

The dataset used in this project contains data from 2 CSV files that are merged together. One contains the primary data for cost of living, and the second provides the detailed headers to clarify what each column represents. The data was then condensed to only show the top 10 cities that we are considering - half of them in Canada (where he is from) and half of them in the US.

- [Cost_of_Living](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living?select=cost-of-living.csv)
- [Cost_of_Living_Headers](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living?select=cost-of-living.csv)

The project will also utilize data obtained from a Google Maps API. To run this within the project, you will need to obtain your own API key by following the instructions in the link below:

- https://developers.google.com/maps/get-started#enable-api-sdk

### Project Structure

The project is organized as follows:

- **Data Exploration:** Jupyter notebooks to explore the dataset.

- **Analysis:** Using Python with the Pandas package to clean the data and perform calculations.

- **Visualizations :** Using Matplotlib / Seaborn to visualize my findings. 

## Features Utilized for the project

  | Feature        | Description                           |
  |----------------|---------------------------------------|
  | Read TWO data files| Used 2 CSV files from kaggle and one from API         |
  | Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.      | Cleaned my data and merged them with pandas. New columns were calculated  based on orignal columns |
  | Make 3 matplotlib / seaborn visulaizations | Made various plots to show off my findings. |
  | Utilize a virtual environment      | Made a venv for this project to keep my computer clean. |
  | Notate your code with markdown cells in Jupyter Notebook | Markdowns included in my jupyter notebook, code is commented also|

## Getting Started

To run this project, follow these steps:

1. Clone the repository: https://github.com/emhess93/US_vs_Canada_Living/
   
2. Create and activate a virtual environment in the project folder using the appropriate commands for your system (see reference below).
   
| Command | Linux/Mac | GitBash |
|---------|-----------|---------|
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |


3. Install the necessary packages: `pip install -r requirements.txt`

4. Navigate to the "data" folder within the project and open the Jupyter Notebook "Summary". Go to the code beneath the Markdown "Get Distances with Google Maps API" and replace the API key placeholder "your key" with the one you obtained in order to run the code.

5. Run the Jupyter notebook and view the findings.

6. Deactivate the virtual environment: `deactivate`

## Dependencies

List any dependencies or libraries used in the project.
