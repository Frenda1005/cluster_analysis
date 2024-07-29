# cluster_analysis
CVI_clustering


# Cluster Analysis App

This Python application allows users to perform clustering analysis on a CSV file. It uses K-means clustering and provides visualizations for the optimal number of clusters using the Elbow Method and Silhouette Score. The results, including the PCA plot and feature distribution plots, are saved to a specified output directory.

## Features

- Upload a CSV file for analysis
- Define the optimal number of clusters using the Elbow Method and Silhouette Score
- Perform K-means clustering
- Save visualizations and clustering results to a specified output directory

## Prerequisites

- Python 3.9 or higher
- Required Python packages:
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn
  - tkinter (usually included with Python)

You can install the required packages using pip:

```bash
pip install pandas scikit-learn matplotlib seaborn

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cluster-analysis-app.git
```

2. Navigate to the project directory:

```bash
cd cluster-analysis-app
```

3. Run the application:

```bash
python cluster.py
```

4. Use the graphical interface to:
   - Upload a CSV file
   - Define the optimal number of clusters
   - Enter the desired number of clusters
   - Perform the analysis and save the results to a specified directory

## How It Works

- **Upload CSV**: Load your data for analysis.
- **Define Cluster Number**: Generates and saves Elbow and Silhouette plots to help determine the optimal number of clusters.
- **Enter Cluster Number**: Input the desired number of clusters based on the plots.
- **Analyze**: Performs the K-means clustering, saves the results (plots and CSV files) to a specified output directory.

## Project Structure

```
cluster-analysis-app/
│
├── cluster.py          # Main application code
├── README.md           # Project documentation
└── requirements.txt    # List of required Python packages
```

## Output

All plots and CSV files will be saved in a subdirectory named `cluster_result` within the directory specified by the user.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

This application uses the following Python libraries:
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)


