# 📝 Handwritten Character Recognition using CNN

A Machine Learning project developed using **TensorFlow** and the **MNIST dataset** to recognize handwritten digits (0–9) with high accuracy.

---

## 📌 Project Overview

This project uses a **Convolutional Neural Network (CNN)** to classify handwritten digits. The model is trained on the famous **MNIST dataset**, which contains thousands of handwritten digit images.

After training, the model can predict the digit present in an input image with excellent accuracy.

---

## 🎯 Features

- Handwritten digit recognition
- CNN-based Deep Learning model
- Trained on the MNIST dataset
- High prediction accuracy (98.83%)
- Saved trained model for future predictions

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

---

## 📂 Project Structure

```
CodeAlpha_HandwrittenCharacterRecognition/
│
├── train_model.py
├── test_model.py
├── handwritten_character_model.keras
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

This project uses the **MNIST Handwritten Digits Dataset**.

- 60,000 Training Images
- 10,000 Testing Images
- Image Size: 28 × 28 Pixels
- Classes: 10 (Digits 0–9)

---

## ⚙️ Model Architecture

The CNN model consists of:

- Reshape Layer
- Conv2D Layer
- MaxPooling Layer
- Conv2D Layer
- MaxPooling Layer
- Flatten Layer
- Dense Layer
- Output Layer (Softmax)

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model

```bash
python train_model.py
```

### 3️⃣ Test the Model

```bash
python test_model.py
```

---

## 📈 Output

Training Accuracy: **99%+**

Test Accuracy:

```
98.83%
```

Prediction Example:

```
Predicted Digit: 7
Actual Digit: 7
```

---

## 💡 Future Improvements

- Support custom handwritten image input
- Improve accuracy using Data Augmentation
- Build a GUI using Tkinter
- Deploy using Flask or Streamlit
- Convert into a Web Application

---

## 👨‍💻 Author

**Aditya Kumar Saini**

B.Tech CSE (AI & ML)

CodeAlpha Machine Learning Internship

---

## ⭐ Repository

If you found this project useful, consider giving it a ⭐ on GitHub. 