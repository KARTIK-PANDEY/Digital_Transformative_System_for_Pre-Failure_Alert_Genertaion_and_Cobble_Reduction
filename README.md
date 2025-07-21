# 🔧 DIGITAL TRANSFORMATIVE SYSTEM FOR ALERT GENERATION AND COBBLE REDUCTION  
### 📍 Using Data & Video Analytics in Bar & Rod Mill (BRM) at Bhilai Steel Plant (BSP)

**🎓 Internship Project | IIT Bhilai**  
**🔬 In collaboration with Bhilai Steel Plant (SAIL)**  
**🧠 Domain:** Industrial AI • Computer Vision • Predictive Maintenance • Real-time Analytics  
**📅 Duration:** [January, 2025] – [July, 2025]  

---

## 🧭 Project Overview

This repository presents a complete AI-powered **Digital Transformation System** developed to improve **quality control**, **safety automation**, and **cobble prevention** in the **Bar and Rod Mill (BRM)** of **Bhilai Steel Plant (BSP)**.

It integrates **machine learning on billet-level process signals** and **deep learning on CCTV video footage** to generate real-time alerts for:
- ⚙️ **Quality Degradation Prediction**
- 🦺 **PPE Non-compliance Detection**
- 🚨 **Cobble Risk Estimation**

---

## 📌 Modules Covered

### 1️⃣ Predictive Quality Analysis of Billets  
- 📈 Uses billet temperature & torque data to estimate UTS, YS, and UTS/YS ratio  
- 📊 Models: XGBoost Regression, Linear Regression, Logistic Classification  
- 🔁 Real-time readiness for live deployment & alerting  

### 2️⃣ PPE Compliance & Action Recognition (CV-based Safety Monitoring)  
- 🎥 YOLOv8 + DeepSORT for detecting helmets, vests, boots in CCTV streams  
- 👣 Multi-person tracking with temporal action context  
- ⚠️ Violation alerting system via Flask-based dashboard  

### 3️⃣ Cobble Risk Detection & Alert Logic  
- 🧪 Signal correlation analysis between billet entry temperature & stand torque  
- 🧮 Threshold-based and deviation-based anomaly detection  
- ⏱️ Works on 50ms resolution time-series data per billet  

---

## 🛠️ Tech Stack

| Domain | Tools & Frameworks |
|--------|--------------------|
| Data Science | Python, Pandas, NumPy, Matplotlib |
| ML/AI | XGBoost, Scikit-learn, PyTorch |
| Computer Vision | YOLOv8 (Ultralytics), DeepSORT, OpenCV |
| Annotation | CVAT, LabelImg |
| Signal Processing | IBA Analyzer, Parquet, .dat decoder |
| Deployment | Flask, Jupyter SSH Servers |
| Visualization | Plotly, Seaborn |

---

## 📁 Repository Structure

