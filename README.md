# AIRBAG-DEPLOYMENT-DETECTION-IN-VEHICLES  

Airbag deployment detection is a vital feature for improving road safety by ensuring rapid response during accidents. This project focuses on detecting airbag deployment using deep learning techniques and automatically notifying emergency services, including police stations, hospitals, and nearby ambulances.

## Overview  

The model is designed to identify airbag deployment in vehicles during accidents by analyzing sensor data and images from in-vehicle cameras. This system provides a proactive approach to accident response, ensuring timely assistance and potentially saving lives.

## Dataset and Training  

The dataset used for this project includes annotated examples of airbag deployments, sourced from custom sensor data and relevant open datasets. Preprocessing ensures that the model is robust and can handle a variety of real-world scenarios.  

The model is trained using a `train_airbag_model.ipynb` notebook on Google Colab. Colab's GPU acceleration significantly speeds up the training process, ensuring efficient convergence of the model.  

## TensorFlow Lite Conversion  

To enable deployment on edge devices, the trained model is converted to TensorFlow Lite format. The conversion script is included in the same notebook. TensorFlow Lite ensures lightweight and efficient model performance on resource-constrained hardware.  

## Deployment and Notification System  

Upon detecting airbag deployment, the system triggers an automated notification, sending alerts to:  
- Local police stations  
- Nearby hospitals  
- Available ambulances  

The notification system is integrated via a real-time messaging protocol, ensuring immediate action.  

## Running the Model  

To use the trained model locally or on an edge device, follow these steps:  

1. Clone this repository:  

    ```bash
    git clone https://github.com/vishnudev-p/airbag-deployment-detection.git  
    cd airbag-deployment-detection  
    ```  

2. Download the TensorFlow Lite model (`airbag_model.tflite`) from the repository.  

3. Run the detection script:  

    ```bash  
    python TFLite_detection_Alert.py --modeldir=custom_model_lite  
    ```  

4. Configure the notification settings in the `config.json` file to include emergency contact details.  

## Demo and Visualization  

A demo video showcasing the system's functionality is available below:  
[Watch the Demo](https://www.youtube.com/watch?v=DEMO_LINK)  

---

This project highlights the use of AI in enhancing vehicle safety and ensuring a swift response during emergencies.
