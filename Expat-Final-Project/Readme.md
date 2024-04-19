# Expat Country Comparison Tool

This tool provides an interactive platform for comparing countries based on various metrics such as GDP, Happiness Index, Life Expectancy, Crime Rate, Death Rate, and Average Temperatures. It allows users to visualize and compare the top 10 countries for retirement based on customized weighting of these metrics.

### Features:

Data cleaning and preprocessing.
Visualization of the top 10 countries by retirement score.
Interactive comparison of two countries across selected metrics.
Weighted comparison of countries based on user-defined priorities.

### Installation:
To run this project, you will need Python installed on your system, along with several third-party libraries.

### Prerequisites:

Python 3.8 or higher
Pip (Python package installer)

### Dependencies

Install all required packages using pip:
pip install pandas gradio matplotlib numpy openpyxl ipywidgets plotly_express geopandas

### Getting Started

#### Prepare the Data:
Ensure that your Excel file with country data is placed in a known directory and update the file paths in the script accordingly.
#### Run the Application:
Open your terminal or command prompt or Jupyter Notebook.
Navigate to the directory containing the script.
Run the script with:

Expat Code.ipynb

### Usage

The application will launch a web interface accessible through your browser at http://localhost:7860.
You can interact with different components:

#### Data Preprocessing: 

Automatically preprocesses the data upon running the script.

#### Visualize Top Countries: Click the button to plot the top 10 countries based on retirement scores.
#### Compare Two Countries: Select two countries from the dropdown menus to compare them across various metrics.
#### Custom Country Comparison: Use sliders to adjust the importance of different metrics and compare any two countries based on these weights.

### Troubleshooting

If you encounter issues related to missing packages, ensure all dependencies are installed as listed in the Dependencies section.
Verify that the Excel files are located in the correct path and are accessible to the script.
Ensure there are no permission issues with the files or directories involved.

### Contributing
Contributions are welcome. Please fork the repository and submit a pull request with your updates.

