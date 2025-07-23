# 🔧 DIGITAL TRANSFORMATIVE SYSTEM FOR PRE-FAILURE ALERT GENERATION AND COBBLE REDUCTION USING DATA AND VIDEO ANALYTICS
### 📍 Using Data & Video Analytics in Bar & Rod Mill (BRM) at Bhilai Steel Plant (BSP)

**🎓 Internship Project @IIT Bhilai**  
**🔬 In collaboration with Bhilai Steel Plant (SAIL)**  
**🧠 Domain:** Industrial AI • Anamoly Detection • Predictive Maintenance • Real-time Analytics  
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
| Signal Processing | IBA Analyzer, .Parquet, .dat decoder |
| Deployment | Flask, Grafana, Jupyter SSH Servers |
| Visualization | Plotly, Seaborn, Matplotlib |

---

## 📁 Repository Structure


---

## 📊 Results & Performance Highlights

### 🔬 Quality Prediction
- **UTS R² Score:** 0.82  
- **YTS Classification Accuracy:** 91%  
- **Critical Features:** Tail Breaker Temp, Stand 1 Torque  

### 🦺 PPE Detection (YOLOv8 + DeepSORT)
- **mAP (Helmet):** 89.4%  
- **Tracking FPS:** 15–20 (edge GPU)  
- **Alerts Triggered:** Real-time on PPE violations

### ⚠️ Cobble Alert Logic
- Stand 1 Entry Temp + Torque signal deviation correlation  
- Threshold-based alert logic with 50 ms sensor resolution  
- Visualization dashboard for mill supervisor insights

---

## 📚 Key Learnings

- Industrial sensor data cleaning & high-frequency (50ms) processing  
- Feature engineering with pyrometer & torque signals  
- Machine learning model tuning for quality prediction  
- YOLOv8 + DeepSORT integration for industrial CV  
- Flask and Grafana-based live alert system with deployment-ready structure  
- Real-time anomaly detection logic for cobble prevention  
- End-to-end research workflow — from raw data to working prototype

---

## 📢 Acknowledgements

- **Guide:** Dr. GAGAN RAJ GUPTA, IIT Bhilai  
- **Industry Partner:** Bhilai Steel Plant (BSP), SAIL  
- **Special Thanks:** R&D Wing, BSP for industrial support and data access  

---

## 📌 License  
This repository is part of a collaborative research internship project.  
For reproduction, deployment, or citation, please contact the author or guide.

---

**🚀 Bridging AI with Steel Industry — For Smarter, Safer, and Stronger Operations.**
