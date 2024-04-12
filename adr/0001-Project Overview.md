# Marine Animal Detection for Investigating the Impact of Wind Farms on Underwater Biodiversity

Date created: 12 Apr 2024

Date revised: TBD

Author(s): Yu Yuen Hern

## Introduction
Man-made structures such as wind farms have been known to impact the environment, including underwater biodiversity. 
This project aims to investigate the impact of wind farm structures on underwater biodiversity by detecting the presence 
of underwater biodiversity in images and videos, and classifying them into different classes and recording the occurrence.

## Objectives
1. To detect the presence of underwater biodiversity in images and videos.
2. To classify the underwater biodiversity into different classes and the occurrence of each class in the image or video.

## Current Approaches
There are no existing studies on the impact of wind farms on underwater biodiversity using computer vision techniques. 
However, there are studies on the detection of marine animals from images and videos, which can be adapted for this project.

Current approaches for detecting marine animals from images and videos include:
1. CNN-based MobileNetV2 with transfer learning (Liu et al., 2018) - [link](https://ieeexplore.ieee.org/document/8867190)
2. Residual CNN with image enhancement methods (Lopez-Vazquez et al., 2023) - [link](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-023-00711-w)
3. ResNet50-Quantum Classical Neural Network (QCNN) (Pravin et al., 2023) - [link](https://www.researchgate.net/publication/376532982_Underwater_Animal_Identification_and_Classification_Using_a_Hybrid_Classical-Quantum_algorithm)
4. Faster R-CNN (accurate but slow) and YOLOv3 (fast but less accurate) (Gu et al., nd.) - [link](http://noiselab.ucsd.edu/ECE228_2019/Reports/Report1.pdf)
5. ResNet50 and BN-Inception (Zhuang et al., nd.)- [link](https://ceur-ws.org/Vol-1866/paper_166.pdf)
6. YOLOv3 (accurate but slow) and YOLOv5 (fast but less accurate) (Zhong et al., 2022) - [link](https://www.researchgate.net/publication/360163279_REAL-TIME_MARINE_ANIMAL_DETECTION_USING_YOLO-BASED_DEEP_LEARNING_NETWORKS_IN_THE_CORAL_REEF_ECOSYSTEM)

Based on the above literature, we should consider:
- Image enhancement methods
- CNN-based model like MobileNetV2 (lightweight), Residual CNN and YOLOv3 (accurate but slow)
- Transfer learning on underwater animal datasets