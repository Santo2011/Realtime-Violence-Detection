# Realtime-Violence-Detection
Realtime Violence Detection WebApp - DL | OPENCV | STREAMLIT
- **Real-Time Violence Detection**: Leveraging a sophisticated deep learning model to analyze and detect violent behaviors in video streams.
- **Frame Capture & Storage**: Automatically captures frames from the video stream, storing them in a dedicated folder for further analysis.
- **Batch Processing**: Utilizes batches of 16 frames for efficient and accurate violence detection.
- **Interactive UI**: A beautifully crafted user interface with Start, Stop, Predict, and Delete buttons for easy control and management.
- **Streamlit WebApp**: Built with Streamlit, ensuring a smooth and responsive experience.

#Implementation
Ensure you have Python installed, then run:
   
  ```
  python -m pip install -r requirements.txt
  ```
Launch the WebApp

```
streamlit run main3.py
```
#Project Structure:
- `main3.py`: The main Streamlit application file.
- `model/`: Directory containing the deep learning model files.
- `frames/`: Folder where captured frames are stored.
- `requirements.txt`: Lists all the Python dependencies.

#NOTE:
Create a folder "model" and download the models from the drive link.
Paste the models into the model folder and make changes in the path accordingly inside the code for the implementation.

link : https://drive.google.com/drive/u/2/folders/1jPz2gibJENk9jrugljdhouIIpwIOyxjH
