import os
import gradio as gr
import PIL.Image as Image

from ultralytics import YOLO

model = YOLO("best.pt")


def predict_image(img, conf_threshold, iou_threshold, image_size):
    """Predicts objects in an image using a YOLOv8 model with adjustable confidence and IOU thresholds."""
    results = model.predict(
        source=img,
        conf=conf_threshold,
        iou=iou_threshold,
        show_labels=True,
        show_conf=True,
        imgsz=image_size,
    )

    for r in results:
        im_array = r.plot()
        im = Image.fromarray(im_array[..., ::-1])

    return im

example_list = [["examples/" + example] for example in os.listdir("examples")]

iface = gr.Interface(
    fn=predict_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold"),
        gr.Slider(
                    label="Image Size",
                    minimum=320,
                    maximum=1280,
                    step=32,
                    value=640,
                )
    ],
    outputs=gr.Image(type="pil", label="Result"),
    title="YOLOv10: Real-Time Fire and Smoke Detection",
    description="This project utilizes the YOLOv10 model to detect Fire and Smoke in Real-Time. Adjust the confidence and IoU thresholds for optimal detection performance. Upload an image to see the detection results.\n [Github](https://github.com/X-Men01/YOLOv10-Fire-and-Smoke-Detection)",
    examples=[
        [example_list[0][0], 0.25, 0.45, 640],
        [example_list[1][0], 0.25, 0.45, 960],
        [example_list[2][0], 0.25, 0.45, 640],
    ],
    allow_flagging="never",
    submit_btn="Run Inference", 
)

if __name__ == "__main__":
    iface.launch()
