import argparse
import os
from ultralytics import YOLO

def run_detection(weights_path, source_path, out_path, conf=0.25):
    model = YOLO(weights_path)
    results = model.predict(
        source=source_path,
        conf=conf,
        save=True,
        project=out_path,  # куда сохранять
        name="pred"        # подпапка внутри out_path
    )
    print(f"Detections saved to {os.path.join(out_path, 'pred')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", type=str, default="best.pt", help="Path to model weights")
    parser.add_argument("--source", type=str, required=True, help="Path to image, video or folder")
    parser.add_argument("--out", type=str, default="runs/detect", help="Output folder")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    args = parser.parse_args()

    run_detection(
        weights_path=args.weights,
        source_path=args.source,
        out_path=args.out,
        conf=args.conf
    )