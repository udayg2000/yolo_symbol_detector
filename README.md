# yolo_symbol_detector

 ======================
| preparing the dataset|
 ======================
- put the symbol images in the directory ./custom_dataset
- download or clone the repository- https://github.com/tzutalin/labelImg
- use the above tool to manually create the xml files required for training which have labels of image and coordintes of bounding box.
- after an xml file has been created for each image divide the dataset into train and test.
- put the train images and the corresponding xml files in the directory ./custom_dataset/train
- put the test images and the corresponding xml files in the directory ./custom_dataset/test
- run python file "tools/XML_to_YOLOv3.py" to generate the text files from the above xml files in the directory "model data".
- the above step would generate three text files "symbols_names.txt", "symbols_test.txt", "symbols_train.txt" in the directory         model_data which would be in the format required for the yolo trining.

 ======================
|    yolo training     |
 ======================
- set all the necessary confugurations (the paths to "symbols_names.txt", "symbols_test.txt", "symbols_train.txt") in the "yolov3/configs.py"
- run "train.py"
- after training the weights are stored in the directory "checkpoints"
- use "tensorboard --logdir=log" and then paste the address given (http://localhost:6006/) to view the tensorboard plots

 ======================
|      detection       |
 ======================
-place the images having symbols to be detected in the folder "symbol_images"
- run "detection_custom.py" to get the use the trained model to detect the symbols in the images






    
 

