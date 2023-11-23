# Student Performance Evaluation on Mathematics 
**Website link:** https://asseelo2000.github.io/Student-Performance-Evaluation-on-Mathematics/
<br>
The Student Performance Analysis System is a machine learning-based solution that analyzes student performance using various features. It leverages a CI/CD pipeline and is yet to deployed on Streamlit for automated development, testing, and deployment.

## Overview

The Student Performance Analysis System utilizes machine learning algorithms to forecast student performance based on factors such as demographics, previous grades, attendance, and other relevant indicators. By analyzing historical data, the system can provide valuable insights to educators, enabling them to identify students who may require additional support or intervention.

## Architecture

The system architecture is as follows:

- Data Ingestion: The system collects student data from various sources, such as databases, files, or APIs, and performs data ingestion to centralize and prepare the data for analysis.
- Preprocessing: The collected data undergoes preprocessing to clean, transform, and normalize it. Missing values are handled, and feature engineering techniques are applied to extract meaningful information.
- Model Training: Machine learning models, such as regression or classification algorithms, are trained using the preprocessed data. Hyperparameter tuning and cross-validation techniques are utilized to optimize model performance.
- Model Evaluation: The trained models are evaluated using appropriate metrics to assess their accuracy, precision, recall, and other relevant indicators. This helps validate the models' effectiveness and identify areas for improvement.
- Deployment: The best-performing model is deployed on Microsoft Azure using a CI/CD pipeline. This pipeline automates the testing, version control, and deployment processes, ensuring seamless integration with the production environment.

## Getting Started

To get started with the Student Performance Analysis System, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/student-performance-prediction.git

2. Set up the Python environment with the required dependencies. It is recommended to use a virtual environment:

    ```shell
    cd student-performance-prediction
    python -m venv env
    source env/bin/activate  # For Unix/Linux
    env\Scripts\activate  # For Windows
    pip install -r requirements.txt

3. Explore the code and Jupyter notebooks in the repository to understand the data preprocessing, model training, evaluation, and deployment steps.

4. Run the notebooks sequentially to execute the code and reproduce the results.



