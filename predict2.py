import cv2
from tensorflow.keras.models import load_model  # type: ignore
import numpy as np
import os
import streamlit as st
from discord_webhook import sendMsg
import os
from dotenv import load_dotenv


# Loading environment
load_dotenv()

# Globals
WEBHOOK_SERVER_URL = os.getenv("WEBHOOK_SERVER_URL")
WEBHOOK_ACCESS_TOKEN = os.getenv("WEBHOOK_ACCESS_TOKEN")


IMAGE_HEIGHT, IMAGE_WIDTH = 64, 64
SEQUENCE_LENGTH = 16
CLASSES_LIST = ["NonViolence", "Violence"]

# Load your trained model
# model = load_model("models\BILSTM_RESNET_MODEL.h5")


def process_frames(
    frames_list, batch_number, MODEL_PATH="models\BILSTM_RESNET_MODEL.h5"
):
    """
    Process and predict the given list of frames, including the batch number in the output.
    """
    model = load_model(MODEL_PATH)
    # frames_array = np.array(frames_list)
    predicted_labels_probabilities = model.predict(np.expand_dims(frames_list, axis=0))[
        0
    ]
    predicted_label = np.argmax(predicted_labels_probabilities)
    predicted_class_name = CLASSES_LIST[predicted_label]

    print(
        f"Batch {batch_number}: Predicted: {predicted_class_name}, Confidence: {predicted_labels_probabilities[predicted_label]:.4f}"
    )

    # print(WEBHOOK_SERVER_URL)

    if predicted_class_name == CLASSES_LIST[1]:
        sendMsg(WEBHOOK_SERVER_URL, WEBHOOK_ACCESS_TOKEN, CLASSES_LIST[1] + " Detected")
    st.write(
        f"Batch {batch_number}: Predicted: {predicted_class_name}, Confidence: {predicted_labels_probabilities[predicted_label]:.4f}"
    )


def predict_frames_from_folder(frames_folder_path, MODEL_PATH):
    frame_paths = [
        os.path.join(frames_folder_path, f)
        for f in os.listdir(frames_folder_path)
        if f.endswith((".png", ".jpg", ".jpeg"))
    ]
    frame_paths.sort()  # Ensure that the frames are sorted in order

    if not frame_paths:  # Check if the frame_paths list is empty
        st.write("No frames available for prediction.")
        return

    frames_list = []
    batch_number = 1  # Initialize batch number

    with st.sidebar:
        for frame_path in frame_paths:
            frame = cv2.imread(frame_path)
            resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
            normalized_frame = resized_frame / 255.0
            frames_list.append(normalized_frame)

            if len(frames_list) == SEQUENCE_LENGTH:
                process_frames(frames_list, batch_number)
                frames_list = []  # Clear the list for the next batch of frames
                batch_number += 1  # Increment batch number

    # Process any remaining frames if they don't make up a full batch of SEQUENCE_LENGTH
    if len(frames_list) > 0:
        # Optional: You could pad this list to be of length SEQUENCE_LENGTH if your model requires it strictly
        process_frames(frames_list, batch_number)


# # UI setup in Streamlit
# st.title("Frame Prediction")
# frames_folder_path = "frames"  # Specify the path to your folder containing frames

# # Button to start prediction
# if st.button("Predict Frames"):
#     predict_frames_from_folder(frames_folder_path)