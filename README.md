Real-Time Credit Card Fraud Detection System

An end-to-end machine learning application engineered to detect fraudulent credit card transactions in real-time. The project features a complete workflow from data analysis and model training to deployment as an interactive web application.

🔴 Live Application: https://umesh-mehtre-fraud-detection-app.streamlit.app/

![alt text](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![alt text](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![alt text](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![alt text](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

Business Problem & Objective

Credit card fraud represents a significant financial risk for banks and their customers. The primary objective of this project was to develop a highly reliable system capable of identifying fraudulent transactions from a vast majority of legitimate ones. The core challenge lies in the severe class imbalance of the dataset, where fraudulent transactions account for less than 0.2% of the total, making traditional accuracy metrics misleading and ineffective.

Core Features

High-Recall ML Model: The system utilizes a Logistic Regression model specifically tuned to maximize the detection of fraudulent cases (high recall), which is the most critical metric for minimizing financial loss.

Interactive Web Interface: A user-friendly web application built with Streamlit allows for real-time transaction simulation and fraud prediction.

End-to-End Deployment: The entire application is containerized and deployed on Streamlit Community Cloud, demonstrating a full project lifecycle from development to production.

Technical Workflow & Methodology

This project was executed through a structured, multi-phase approach:

1. Exploratory Data Analysis (EDA) & Preprocessing

Challenge Identification: The initial analysis immediately revealed the critical class imbalance (99.8% non-fraudulent vs. 0.17% fraudulent), confirming that accuracy would be a deceptive evaluation metric.

Feature Scaling: Applied StandardScaler to the Time and Amount features to ensure their scale did not disproportionately influence the model's learning process.

2. Model Development & Training

Data Splitting Strategy: Implemented a stratified train_test_split to maintain the same class distribution in both training and testing sets, preventing model bias and data leakage.

Imbalance Handling: The LogisticRegression model was instantiated with the class_weight='balanced' parameter. This technique penalizes misclassifications of the minority (fraud) class more heavily, compelling the model to prioritize its detection.

3. Model Evaluation Strategy

Beyond Accuracy: The evaluation deliberately focused on metrics suitable for imbalanced datasets.

Key Metrics: The Confusion Matrix was analyzed to understand the types of errors, with a primary focus on minimizing False Negatives (missed fraud cases). The Classification Report provided the crucial Recall and Precision scores for the fraud class. The final model was optimized to achieve a high recall score.

4. Application Deployment

API & Interface: Developed an intuitive user interface using Streamlit, allowing users to input transaction features and receive instant predictions.

Version Control & CI/CD: Utilized Git and GitHub for version control. The deployment to Streamlit Community Cloud is automated, triggering a rebuild upon every push to the main branch.

Key Deployment Challenges & Resolutions

Developing the model was only half the journey. Deploying it involved overcoming several significant technical hurdles, demonstrating robust problem-solving and debugging skills.

Problem	Resolution
GitHub's 100MB File Limit	Implemented Git Large File Storage (LFS) to manage and version control the 144MB dataset and model artifacts (.pkl), which would otherwise be rejected by GitHub.
Persistent ModuleNotFoundError	Diagnosed a critical environment issue where the default Python version (3.13) on the deployment server had compatibility problems. Resolved by creating a runtime.txt file to explicitly force the use of the stable Python 3.11 environment.
Dependency Conflicts	The initial requirements.txt generated via pip freeze contained local Windows paths, causing installation failures. Refactored the file to be a clean, minimal list of core packages, ensuring universal compatibility.
OS Case-Sensitivity Bug	Discovered and resolved a subtle but critical bug where two requirement files (requirement.txt and requirements.txt) existed in the repo due to Windows' case-insensitivity. Removed the incorrect file using git rm to enforce a single, correct dependency source.
Technology Stack

Core Development: Python 3.11

Data Science & ML: Pandas, NumPy, Scikit-learn

Web Framework: Streamlit

Version Control: Git, GitHub, Git LFS

Deployment Platform: Streamlit Community Cloud

How to Run This Project Locally

Clone the repository:

code
Bash
download
content_copy
expand_less

git clone https://github.com/umeshmehtre/fraud-detection-streamlit-app.git
cd fraud-detection-streamlit-app

Install the required dependencies:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
pip install -r requirements.txt

Run the Streamlit application:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
streamlit run app.py
