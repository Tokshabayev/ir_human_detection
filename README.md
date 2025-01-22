# Infrared Human Detection

This project provides an object detector (primarily targeting **human detection**) for **infrared (IR)** images and videos using [Ultralytics YOLOv8s model](https://github.com/ultralytics/ultralytics). The model helps detect people under **challenging conditions**, such as low visibility, nighttime, smoke, or fog.

## Why Infrared Cameras?

1. **Low-Light or Nighttime**  
   IR cameras capture **thermal** emission from objects, making them independent of ambient light. Even in total darkness, humans or animals appear bright against cooler backgrounds.

2. **Smoke and Fog Penetration**  
   In visible light, thick smoke or fog can obscure objects. IR (thermal) waves often penetrate these conditions more effectively, maintaining the ability to detect warm bodies.

3. **Camouflage and Contrast**  
   Even if an object is camouflaged visually, it can still be **distinguished by temperature** differences in the IR spectrum.

4. **Security and Safety**  
   For perimeter monitoring, search-and-rescue missions, or night patrols, thermal cameras are essential to detect threats or missing persons in near or total darkness.

---

## Training Dataset and Metrics

- I trained the model on a **custom IR image dataset**, depicting humans in various conditions.  
- During training, we used **YOLOv8** with standard hyperparameters and moderate augmentations (Mosaic, Mixup).  
- The **key metrics** achieved on the validation set:
  - **Precision**: ~0.88  
  - **Recall**: ~0.87  
  - **mAP@0.5**: ~0.93  
  - **mAP@0.5:0.95**: ~0.62  

These metrics indicate that the model can reliably detect people (high mAP@0.5) while maintaining a good balance between Precision and Recall.

---

## Project Contents

- **`detect.py`** – Main detection script using Ultralytics YOLOv8.  
- **`Dockerfile`** – Dockerfile for building a GPU-enabled (CUDA) image.  
- **`data/`** – Example input files (IR images/videos) and output results.

---

## Building the Docker Image

> **Note**: This setup assumes **GPU acceleration**. Ensure:
> - You have [NVIDIA drivers](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html) installed on the host,  
> - [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) is set up,  
> - You have a compatible GPU.

1. Clone or copy the repository files into a folder.
2. Navigate to that folder in a terminal.
3. Build the Docker image (named `ir_bbox` here):

    ```
    docker build -t ir_bbox:latest .
    ```

4. Confirm the image is built:

    ```
    docker images
    ```

---

## Running the Container

Below are examples for **Windows** (PowerShell or CMD) and **Linux/macOS**.  
Assume you have a local `data/` folder for input and output.

### 1. Windows PowerShell

Run:

    docker run --gpus all --rm -it `
        -v "${pwd}/data:/data" `
        ir_bbox:latest `
        --source /data/videotest.mp4 `
        --out /data/out `
        --conf 0.3

- `--gpus all` enables GPU access in the container.  
- `-v "${pwd}/data:/data"` mounts the local folder `data` into `/data`.  
- `--source /data/videotest.mp4` is the IR video file to process.  
- `--out /data/out` is where detection results are saved.  
- `--conf 0.3` sets the confidence threshold for detections.

### 2. Windows CMD

Use `%cd%` instead of `${pwd}`:

    docker run --gpus all --rm -it ^
        -v "%cd%/data:/data" ^
        ir_bbox:latest ^
        --source /data/videotest.mp4 ^
        --out /data/out ^
        --conf 0.3

### 3. Linux / macOS

    docker run --gpus all --rm -it \
        -v "$(pwd)/data:/data" \
        ir_bbox:latest \
        --source /data/videotest.mp4 \
        --out /data/out \
        --conf 0.3

> Without a GPU or with a CPU-only build, omit `--gpus all` and ensure the image supports CPU inference.

---

## Contributing and Feedback

- **Issue Tracker**: Please open an issue for bugs or feature requests.  
- **Pull Requests**: Contributions for improving detection, adding more training data, or enhancing scripts are welcome.  
- **Contact**: For direct questions, feel free to file an issue or reach out via this repository.

---

## License

Distributed under an open-source license (e.g., MIT or Apache 2.0). Check the [LICENSE](LICENSE) file for details.

---

### Acknowledgments

- Thanks to [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8.  
- Infrared images courtesy of open-source IR datasets and/or collected IR footage.

