# End-to-End Credit Card Fraud Detection Project 💳

This project is a complete end-to-end demonstration of building a machine learning model to detect credit card fraud, deploying it as an interactive web application, and overcoming the many real-world challenges that come with it.

### 🔴 **Live Application:** [**https://umesh-mehtre-fraud-detection-app.streamlit.app/**](https://umesh-mehtre-fraud-detection-app.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

## The Goal

The mission was to build an intelligent system that could analyze the details of a credit card transaction and flag it as either fraudulent or legitimate. The primary challenge was that fraud is like finding a **needle in a haystack**—it's incredibly rare. This meant a simple model wouldn't work; a more strategic approach was required.

---

## My Journey Through This Project

This project wasn't just about writing code. It was a step-by-step process of discovery, strategic decision-making, and extensive debugging.

### Phase 1: Data Exploration & Strategy

It all started with the data from Kaggle. My first steps were to explore it using Pandas to understand the landscape.

*   **The Critical Discovery:** I immediately identified the project's core challenge. By counting the occurrences of normal vs. fraudulent transactions, I found that **over 99.8% of the data was non-fraudulent**.
*   **The 99% Accuracy Trap:** This discovery was pivotal. It meant a naive model that always guessed "not fraud" would still be 99.8% accurate. This taught me my first big lesson:
    > **Accuracy is a fundamentally misleading metric for this problem and must be ignored.**

### Phase 2: Building a Model (The Right Way)

Armed with insights about the data imbalance, I proceeded with a careful modeling strategy.

1.  **Preprocessing:** The `Time` and `Amount` columns were on a different scale from the other features. I used `StandardScaler` from Scikit-learn to normalize them, preventing them from disproportionately influencing the model.
2.  **The Golden Rule:** I learned that you **must** split data into training and testing sets *before* any other operations. I used `stratify=y` to ensure the training and testing sets both had the same tiny percentage of fraud cases, preventing data leakage and bias.
3.  **Handling Imbalance:** Instead of complex methods, I used a powerful parameter in `LogisticRegression`: `class_weight='balanced'`. This instructs the model to significantly increase the penalty for misclassifying the rare fraud cases, forcing it to pay much closer attention to them.

### Phase 3: Finding the Truth - A Proper Evaluation

With the model trained, it was time for a real-world evaluation. I disregarded accuracy and used superior metrics:

*   **The Confusion Matrix:** This provided a raw breakdown of performance, showing me how many frauds I correctly caught (**True Positives**) and, more importantly, how many I missed (**False Negatives**).
*   **The Classification Report:** This was the model's true report card. I focused on two scores for the **`Fraud`** class:
    *   `Precision`: When my model predicted "Fraud", how often was it correct?
    *   `Recall`: Of all the *actual* frauds that occurred, what percentage did my model successfully catch? For a bank, this is the most critical business metric.

My final model achieved a **high Recall**, confirming it was successful at its primary objective: catching fraudsters.

### Phase 4: The Deployment Gauntlet - From Localhost to Live App

Building the model was only half the battle. Deploying it to the cloud was a new adventure that tested my debugging skills extensively. This was the hardest, but most valuable, part of the project.

| Problem | Resolution |
| :--- | :--- |
| **GitHub's 100MB File Limit** | The 144MB dataset was too large for a standard `git push`. **Resolved by integrating Git Large File Storage (LFS)** to manage and version control the large `.csv` and `.pkl` files. |
| **Persistent `ModuleNotFoundError`** | The app kept crashing, unable to find the `joblib` library. After extensive debugging, I diagnosed an environment conflict: the server was using an unstable Python version (3.13). **Resolved by creating a `runtime.txt` file to lock the environment to the stable Python 3.11.** |
| **Dependency & Environment Conflicts** | The initial `requirements.txt` was not portable and contained local paths. **Refactored the file to be a clean, minimal list of core packages**, ensuring a reproducible build on any machine. |
| **OS Case-Sensitivity Bug** | A subtle bug caused by `requirement.txt` and `requirements.txt` coexisting in the repo (due to Windows' case-insensitivity) was breaking the build. **Removed the incorrect file using `git rm` to enforce a single, correct dependency source.** |

---

## How to Run This Project Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/umeshmehtre/fraud-detection-streamlit-app.git
    cd fraud-detection-streamlit-app
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Technology Stack

*   **Language:** Python
*   **Data Analysis:** Pandas, NumPy
*   **Machine Learning:** Scikit-learn
*   **Web App Framework:** Streamlit
*   **Version Control:** Git & GitHub (with Git LFS)
*   **Deployment:** Streamlit Community Cloud
