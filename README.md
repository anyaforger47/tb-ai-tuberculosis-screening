 AI-Based Tuberculosis Screening from Chest X-Rays
 Project Overview

This project implements an AI-based Tuberculosis (TB) screening system using chest X-ray images.
The system leverages a Convolutional Neural Network (CNN) to classify X-rays as TB-positive or Normal and is deployed as a web application using Streamlit.

The goal of this project is to demonstrate an end-to-end medical AI pipeline, including data preprocessing, model training, evaluation using clinical metrics, and real-world deployment considerations.

 Important: This system is designed as a screening aid, not a diagnostic tool.

 Objectives

Build a deep learning model to detect TB patterns in chest X-rays

Evaluate performance using clinically relevant metrics

Deploy the model as an interactive web application

Understand and document real-world limitations of medical AI models

🧠 Model Description

Architecture: Custom CNN (TensorFlow / Keras)

Input: Frontal chest X-ray images

Output: Probability score indicating TB risk

Decision: Binary classification (TB / Normal)

The model predicts a probability score, which is mapped to:

Low TB Risk

High TB Risk

📊 Evaluation Metrics

The model was evaluated on a held-out test set using:

Accuracy: ~98%

Sensitivity (Recall for TB): ~92%

Specificity: ~99%

These metrics indicate strong performance on in-distribution data from the same dataset.

🌍 Deployment

The application is deployed using Streamlit Community Cloud.

Deployment Features:

Web-based image upload

Automatic image preprocessing

Real-time prediction with probability score

Medical disclaimer included

Dynamic model loading from external storage (Google Drive) to handle large model files

🔗 Live App: https://tb-ai-tuberculosis-screening-4a6valmxhhvgpl8nlwbmkw.streamlit.app/

🗂️ Project Structure
tb-ai-tuberculosis-screening/
│
├── app.py                # Streamlit application
├── requirements.txt      # Python dependencies
├── notebooks/            # Data exploration & model training
├── README.md             # Project documentation
└── .gitignore

⚙️ How to Run Locally
pip install -r requirements.txt
streamlit run app.py


The model file is downloaded automatically at runtime.

⚠️ Known Limitations 

This project intentionally documents its limitations to reflect real-world medical AI challenges:

The model performs best on in-distribution data (images similar to the training dataset)

Performance may degrade on external chest X-rays due to:

Dataset bias

Differences in X-ray machines and acquisition protocols

Variability in TB presentation (early-stage, atypical TB, effusions)

No lung segmentation is applied; the model processes the full image

The system must not be used for clinical diagnosis

These limitations highlight the challenge of domain shift, a well-known problem in medical imaging AI.

🏥 Medical Disclaimer

This application is intended for educational and research purposes only.
It is not a diagnostic tool and must not be used for clinical decision-making.
Predictions should always be interpreted by qualified medical professionals.

🧪 Technologies Used

Python

TensorFlow / Keras

OpenCV

NumPy

Streamlit

Google Drive (model hosting)

GitHub

📌 Key Learnings

End-to-end ML system design

Handling large model artifacts in cloud deployment

Importance of sensitivity and specificity in medical AI

Real-world generalization challenges in deep learning


👤 Author

Neha J
Computer Science Student | AI & Medical Imaging Enthusiast
