##LeagueVision
League of Legends is the most popular multiplayer online battle arena (MOBA) game, with a significant global E-sports scene. Because of it's high complexity and it's strategic pertinence, it is subject to lots of analysis. The most important aspects of the game state are the locations of the champions on the map, which highly reflect the strategies, intentions, and future outcomes in the game. This project provides a way to collect positions of players over the course of a game, which can be used to develop, compare, and analyze strategies.

#Generating data (Step 1 of 2)
The first part of the pipeline generates augmented training data using game image assets found online. These generated images visually simulate potential states of the map, by overlaying champion icons onto the map in random locations. Up to five champions with their classes (which champion it is) and bounding boxes (location on the map) are saved in corresponding label files formatted for yolov5.

To complete this step, run generatedata.py. This will generate folders of images and labels. If needed, I would only recommend changing the num_images parameter to control the amount of images to generate. 50,000 samples is the amount I used to achieve great results with only 1 epoch.

#Training the model (Step 2 of 2)
trainyolo.py splits the data into training and validation sets, and creates a dataset.yaml file to configure yolov5 for training. 

After running trainyolo.py, you can run the following command to train the model. 

python yolov5\\train.py --img 640 --batch 32 --epochs 1 --data dataset.yaml --cfg yolov5s.yaml --weights yolov5s.pt --name yolov5s_results

The results will be saved in yolov5/runs/train folder.




##Dependencies
pip install yolov5

