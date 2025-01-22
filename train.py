from ultralytics import YOLO


def train():
    weights = "yolov8s.pt"

    model = YOLO(weights)


    model.train(
        data="thermal2/data.yaml",
        epochs=200,
        imgsz=640,
        batch=32,
        patience=20,
        lr0=0.001,
        lrf=0.01,
        momentum=0.937,
        weight_decay=0.0008,
        warmup_epochs=3,
        warmup_momentum=0.8
    )

if __name__ == '__main__':
    train()

