# ppe_detect_alert.py
# PPE Detection + Popup Alerts (Image-based, no sound)

from ultralytics import YOLO
import ctypes    # for popup alert (Windows only)
import cv2

# Load trained YOLO model
print("[INFO] Loading PPE detection model...")
model = YOLO("yolov8s.pt")

# Input image (change path as needed)
image_path = "images/val/image628.jpg"

results = model.predict(source=image_path, show=True, conf=0.5)

# Define required PPE items (must match your dataset class names)
required_ppe = ["helmet", "vest", "gloves", "boots", "goggles"]

detected_ppe = set()

# Process detections
for r in results:
    boxes = r.boxes
    for box in boxes:
        cls_id = int(box.cls[0])             # class ID
        label = model.names[cls_id]          # label name (helmet, vest, etc.)
        conf = float(box.conf[0])            # confidence score
        print(f"Detected: {label} ({conf:.2f})")
        detected_ppe.add(label.lower())

print("\n[RESULT] PPE Status Check:")
missing_items = []
for item in required_ppe:
    if item in detected_ppe:
        print(f"✅ {item.capitalize()} detected")
    elif f"no_{item}" in detected_ppe:
        print(f"❌ {item.capitalize()} missing (no_{item} detected)")
        missing_items.append(item)
    else:
        print(f"❌ {item.capitalize()} missing (not detected)")
        missing_items.append(item)


# Popup alert if something is missing
if missing_items:
    alert_msg = "⚠ PPE Alert! Missing: " + ", ".join(
        [i.capitalize() for i in missing_items]
    )
    print(alert_msg)

    # Show popup (Windows only)
    ctypes.windll.user32.MessageBoxW(0, alert_msg, "PPE Alert", 1)

# Save output image
annotated_img = results[0].plot()
cv2.imwrite("ppe_output.jpg", annotated_img)

print("\n[INFO] Detection complete. Results saved to ppe_output.jpg")

