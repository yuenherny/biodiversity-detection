# Detecting the Presence of Biodiversity in the Ocean

**Preparation for Ørsted Hack-Ø-Thon 2024:** Investigating the impact of wind farm structures on underwater biodiversity.

**Objectives:**
1. To detect the presence of underwater biodiversity in images and videos.
2. To classify the underwater biodiversity into different classes, and the occurrence of each class in the image or video.

## Getting started
1. Clone the repository.
2. Create a Python environment, activate it and install the requirements.
    ```bash
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
    ```
3. Setup your Kaggle API credentials, see [here](https://www.kaggle.com/docs/api).
4. Run `download_data.py` to download the data.
    ```bash
        python download_data.py
    ```
5. To perform computer vision tasks, it is recommended to have NVIDIA GPU support. If you have a 
    NVIDIA GPU:
    ```bash
        python check_gpu.py
    ```
    You should get an output similar to:
    ```
    CUDA is available: True
    CUDA device count: <An arbitrary number>
    CUDA current device: <An arbitrary number>
    CUDA device name: <An arbitrary string>
    ```
