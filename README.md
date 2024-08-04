<h1 align="center"><span>YOLOv10-Fire and Smoke Detection</span></h1> 
This project focuses on real-time detection and tracking of fires and smoke in video feeds using the latest YOLOv10 model. in this repository includes all the necessary code and resources to implement and demonstrate a robust fire and smoke detection system, showcasing the capabilities of the YOLOv10 model.




https://github.com/user-attachments/assets/49dc1fdc-4312-4851-924c-6eb17cf8ccc1


<h1 align="center"><span>Hugging Face Demo</span></h1> 

To see the model in action, you can test it through [Hugging Face demo](https://huggingface.co/spaces/X-Men01/YOLOv10-Fire-and-Smoke-Detection).

<img width="1440" alt="Screenshot 2024-07-25 at 6 28 26 AM" src="https://github.com/user-attachments/assets/3a7af190-9546-47ee-a47e-cf695d5c99e1">

<h1 align="center"><span>Data</span></h1> 

The dataset used for this project consists of images containing fire and smoke,primarily collected from [Roboflow](https://universe.roboflow.com). To ensure the quality and reliability of the dataset, we performed an extensive data cleaning process using the [cleanvision](https://github.com/cleanlab/cleanvision) library.
#### Data Cleaning Process
The data cleaning process was thoroughly documented in a Jupyter notebook. You can find the notebook, which includes all the code and results, [here](https://github.com/X-Men01/YOLOv10-Fire-and-Smoke-Detection/blob/main/clean_dataset_with_cleanvision_libary.ipynb).
#### Data Download
You can download the dataset used in this project from the following link: [Download Dataset](https://drive.google.com/file/d/1-pu5UUoXMoLDKMWcoF_VTllapISFslX0/view?usp=sharing).

#### cleanvision_report
![cleanvision_report](https://github.com/user-attachments/assets/31d2d8cf-42f8-4e00-8d73-1f17727faa5e)

### Dataset Statistics
Total Number of Images After cleaning: 123,015  
Distribution of Labels:

<img width="458" alt="Screenshot 2024-07-29 at 2 50 03 PM" src="https://github.com/user-attachments/assets/f0bbc491-6e33-4388-bfb9-712d1bc6f498">

<h1 align="center"><span>Training and Validation Metrics</span></h1> 

#### Precision, Recall, and mAP50
To further evaluate the model's performance, we measure precision, recall, and mean Average Precision at 50% IoU (mAP50). These metrics help assess the accuracy and reliability of the model in detecting and classifying fire and smoke in images.

- **Precision**: The ratio of true positive detections to the total number of positive detections (both true and false). It indicates how many of the predicted fires or smoke instances are correct.
- **Recall**: The ratio of true positive detections to the total number of actual positive instances. It shows how well the model captures all the instances of fire and smoke.
- **mAP50**: The mean Average Precision at 50% Intersection over Union (IoU) is a comprehensive metric that combines precision and recall, providing a single score to evaluate the model's overall performance.
![results](https://github.com/user-attachments/assets/2190b80d-e110-49f0-ba58-50a3a9d4d1fa)


<h1 align="center"><span>Model</span></h1>

The trained YOLOv10 model for fire and smoke detection is provided in this repository. You can download and use the pre-trained model to perform fire and smoke detection on your own images or videos.

The model weights can be downloaded from the link below: [Download YOLOv10 Model Weights](https://github.com/X-Men01/YOLOv10-Fire-and-Smoke-Detection/tree/main/models)





