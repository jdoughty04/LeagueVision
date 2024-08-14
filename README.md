# LeagueVision
League of Legends is the most popular multiplayer online battle arena (MOBA) game, with a significant global E-sports scene. Because of it's complexity and strategic pertinence it is subject to lots of analysis, and the most important aspects of the game are the locations of the champions which highly reflect the strategies, intentions, and future outcomes within the game. This project introduces a way to collect positions of players over the course of a game, which can be used to develop, compare, and analyze strategies.

## Dependencies
pip install yolov5

Note that CUDA setup is recommended to run this locally with GPU. 

## Generating data (Step 1 of 2)
The first part of the pipeline generates augmented training data using game image assets found online. These generated images simulate potential states of the map by overlaying champion icons onto the map in random locations. Up to five champions with their classes (which champion it is) and bounding boxes (location on the map) are saved in corresponding label files formatted for yolov5.

To complete this step, run generateData.py. This will generate folders of images and labels. 30,000 images are generated by default, which worked well with 20 epochs.

## Training the model (Step 2 of 2)
trainYolo.py splits the data into training and validation sets, and creates a dataset.yaml file to configure yolov5 for training. 

After running trainYolo.py, you can run the following command to train the model. 

python yolov5\train.py --img 640 --batch 32 --epochs 20 --data dataset.yaml --cfg yolov5s.yaml --name yolov5s_results

The results will be saved in the yolov5/runs/train folder.

See yolov5/detect.py for examples of how to use the trained model to detect champions in a new image/video/etc.


## See it in action
detectInGame.py is a sample program that uses the trained model to overlay bounding boxes in game. Make sure to specify which classes to detect in the 'desired_classes' list. It captures the League of Legends window and shows detections in real time. This is imperfect and certain components of the UI may get in the way of detections. It is also not recommended to use this in game, as it may be against the terms of service.


This clip shows the program in action, with the enemy champions being detected in game.
![detections](/detections.gif)

## Limitations
League of Legends sometimes implements changes, and adds new champions which could change the efficacy of this pipeline. The icons used are from a previous patch, and while most of them are viable, a few are outdated and some champions are missing. This could be fixed, but it would require manual effort to update the icons.
