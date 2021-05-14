#================================================================
#
#   File name   : configs.py
#
#================================================================

# YOLO options
YOLO_DARKNET_WEIGHTS        = "./model_data/yolov3.weights"
YOLO_COCO_CLASSES           = "./model_data/coco.names"
YOLO_STRIDES                = [8, 16, 32]
YOLO_IOU_LOSS_THRESH        = 0.5
YOLO_ANCHOR_PER_SCALE       = 3
YOLO_MAX_BBOX_PER_SCALE     = 100
YOLO_INPUT_SIZE             = 416
YOLO_ANCHORS                = [[[10,  13], [16,   30], [33,   23]],
                               [[30,  61], [62,   45], [59,  119]],
                               [[116, 90], [156, 198], [373, 326]]]
# Train options
TRAIN_CLASSES               =  "./model_data/symbols_names.txt"
TRAIN_ANNOT_PATH            = "./model_data/symbols_train.txt"

TRAIN_LOGDIR                = "./log"
TRAIN_LOAD_IMAGES_TO_RAM    = False # faster training, but need more RAM
TRAIN_BATCH_SIZE            = 4
TRAIN_INPUT_SIZE            = 416
TRAIN_DATA_AUG              = True
#TRAIN_TRANSFER              = False
TRAIN_TRANSFER              = True
TRAIN_FROM_CHECKPOINT       = False # "./checkpoints/yolov3_custom"
#TRAIN_LR_INIT               = 1e-4
TRAIN_LR_INIT               = 1e-4
TRAIN_LR_END                = 1e-6
TRAIN_WARMUP_EPOCHS         = 2
#TRAIN_EPOCHS                = 30
TRAIN_EPOCHS                = 40

# TEST options
TEST_ANNOT_PATH             = "./model_data/symbols_test.txt"
TEST_BATCH_SIZE             = 4
#TEST_BATCH_SIZE             = 29
TEST_INPUT_SIZE             = 416
TEST_DATA_AUG               = False
TEST_DECTECTED_IMAGE_PATH   = "./data/detection/"
TEST_SCORE_THRESHOLD        = 0.3
TEST_IOU_THRESHOLD          = 0.45
#TEST_SCORE_THRESHOLD        = 0.2
#TEST_IOU_THRESHOLD          = 0.4