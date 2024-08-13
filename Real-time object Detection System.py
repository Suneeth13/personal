import os
import cv2
import numpy as np
from pathlib import Path
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import urllib.request

def ensure_directory_exists(directory):
    """Ensure the specified directory exists, creating it if necessary."""
    Path(directory).mkdir(parents=True, exist_ok=True)
    print(f"Directory ensured: {directory}")

def download_file(url, destination):
    """Download a file from a URL to a destination."""
    print(f"Downloading from {url}...")
    urllib.request.urlretrieve(url, destination)
    print("Download complete.")

def verify_file_size(file_path, expected_size):
    """Verify if the file at the given path has the expected size."""
    return Path(file_path).is_file() and Path(file_path).stat().st_size == expected_size

def load_mobilenetv2_model(weights_path):
    """Load the MobileNetV2 model with specified weights."""
    try:
        model = MobileNetV2(weights=weights_path)
        print("MobileNetV2 model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading MobileNetV2 model: {e}")
        exit()

def preprocess_frame(frame):
    """Preprocess a frame for prediction."""
    frame = cv2.resize(frame, (224, 224))
    frame = preprocess_input(frame)
    frame = np.expand_dims(frame, axis=0)
    return frame

def process_video_frames(model):
    """Process video frames for object detection."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        exit()

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    desired_width = 800  # Adjust this value as needed

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error reading frame. Exiting...")
                break

            preprocessed_frame = preprocess_frame(frame)
            if preprocessed_frame is None:
                continue

            predictions = model.predict(preprocessed_frame)
            decoded_predictions = decode_predictions(predictions, top=3)

            labels = [label for (_, label, _) in decoded_predictions[0]]
            cv2.putText(frame, f"Predictions: {', '.join(labels)}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            resized_frame = cv2.resize(frame, (desired_width, int(desired_width * frame_height / frame_width)))
            cv2.imshow('Object Detection', resized_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting...")
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    weights_dir = Path("C:/Users/Suneeth/Desktop/ML")
    weights_path = weights_dir / "mobilenet_v2_weights.h5"
    weights_url = "https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5"
    expected_size = 14536120  # Expected size of the weights file in bytes

    ensure_directory_exists(weights_dir)
    if not verify_file_size(weights_path, expected_size):
        download_file(weights_url, weights_path)

    model = load_mobilenetv2_model(str(weights_path))
    process_video_frames(model)
