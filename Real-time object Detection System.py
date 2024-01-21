import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import os
import requests

# Function to download the weights file
def download_weights(url, destination):
    response = requests.get(url, stream=True)
    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

# URL and path for MobileNetV2 weights
weights_url = "https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5"
weights_path = "C:\\Users\\Suneeth\\Desktop\\ML\\mobilenet_v2_weights.h5"

# Check if weights file exists, if not, download it
if not os.path.isfile(weights_path):
    print("Downloading MobileNetV2 weights...")
    download_weights(weights_url, weights_path)
    print("Download complete.")

# Load MobileNetV2 model with downloaded weights
try:
    model = MobileNetV2(weights=weights_path)
    print("MobileNetV2 model loaded successfully.")
except Exception as e:
    print(f"Error loading MobileNetV2 model: {str(e)}")

# Open video capture
ss = cv2.VideoCapture(0)

# Function for preprocessing frames
def preprocessing_frame(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = preprocess_input(frame)
    frame = np.expand_dims(frame, axis=0)
    return frame

# Get the default window size
frame_width = int(ss.get(3))
frame_height = int(ss.get(4))

# Set the desired width of the output window
desired_width = 800  # You can adjust this value

while True:
    ret, frame = ss.read()

    if ret:
        preprocessed_frame = preprocessing_frame(frame)
        prediction = model.predict(preprocessed_frame)
        decoded_predictions = decode_predictions(prediction, top=3)

        for i, (_, label, score) in enumerate(decoded_predictions[0]):
            print(f"Prediction {i + 1}: {label} (Score: {score:.2f})")

        cv2.putText(frame, f"Predictions: {', '.join([label for (_, label, _) in decoded_predictions[0]])}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Resize the frame for display
        resized_frame = cv2.resize(frame, (desired_width, int(desired_width * frame_height / frame_width)))
        cv2.imshow('Object Detection', resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error reading frame. Exiting...")
        break

# Release video capture and close all windows
ss.release()
cv2.destroyAllWindows()
