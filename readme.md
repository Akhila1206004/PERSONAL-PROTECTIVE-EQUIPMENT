#### **Personal Protective Equipment (PPE) Detector – Construction site safety**

“Safety first, always.”



This project detects whether construction workers are wearing helmets, gloves, vests, boots, and goggles using YOLOv8. It can also flag missing PPE in images, videos, or live webcam feeds.



######  **Why I built this**



Construction sites can be risky, and manual monitoring is slow and error-prone.

I wanted to make a quick AI tool that helps spot safety violations automatically.



######  **How I made it**



Dataset: Collected PPE images (helmet, gloves, vest, boots, goggles, and missing PPE).



Configuration: Created data.yaml for YOLOv8.



   **Install YOLO (Ultralytics)**

        [*pip install ultralytics*](pip install ultralytics)



    **Verify installed**

           [*yolo --version*](yolo --version)



      **Training: Ran YOLOv8 on CPU (slow but works!)**



&nbsp;       [\[yolo train data=dataset/data.yaml model=yolov8s.pt epochs=5 imgsz=256](yolo train data=dataset/data.yaml model=yolov8s.pt epochs=5 imgsz=256)]([yolo train data=dataset/data.yaml model=yolov8s.pt epochs=5 imgsz=256](yolo train data=dataset/data.yaml model=yolov8s.pt epochs=5 imgsz=256))



       **Trained model weights are saved at:**

&nbsp;      [runs/detect/trainX/weights/best.pt](runs/detect/trainX/weights/best.pt)



###### **🚀 How to use it**



Run on an image:



*yolo predict model=runs/detect/trainX/weights/best.pt source="image.jpg"*





Run on webcam:



*yolo predict model=runs/detect/trainX/weights/best.pt source=0*





Run on video:



*yolo predict model=runs/detect/trainX/weights/best.pt source="video.mp4"*



######  **Current Status**



* Model Training Completed – trained for 5 epochs using YOLOv8.

* &nbsp;Detects PPE (Helmet \& Vest) and also identifies missing PPE.
* Runs on CPU smoothly (no GPU required).
  Tested on images – outputs are saved automatically in runs/detect/predict/.
* Good detection accuracy even with a small number of training epochs.
* &nbsp;Ready for extension to video streams or real-time webcam input.



###### **🌟 Future Plans**



* Train with a larger dataset \& more epochs for better accuracy.
* 
* Extend detection to more PPE items (gloves, masks, goggles, safety shoes).
* 
* Deploy on real-time CCTV/webcam feeds for live monitoring.
* 
* Build a simple web or mobile app for supervisors to check PPE compliance.
* 
* Add alerts \& reports for automatic safety violation tracking.







