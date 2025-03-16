# # from pptx import Presentation
# # from pptx.util import Inches
# # from pptx.enum.text import PP_ALIGN
# # from pptx.dml.color import RGBColor
# # from pptx.chart.data import CategoryChartData
# # from pptx.enum.chart import XL_CHART_TYPE
# # from pptx.enum.shapes import MSO_SHAPE
# # import cv2
# # import numpy as np
# # import matplotlib.pyplot as plt

# # # Function to generate dynamic image graphics
# # def generate_image(image_path, output_path):
# #     # Read the image
# #     img = cv2.imread(image_path)
# #     # Convert to grayscale
# #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #     # Apply threshold
# #     _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# #     # Save the processed image
# #     cv2.imwrite(output_path, thresh)

# # # Create a presentation object
# # presentation = Presentation()

# # # Helper function to add title and content to slides
# # def add_slide(title, content, is_title_slide=False):
# #     slide_layout = presentation.slide_layouts[0] if is_title_slide else presentation.slide_layouts[1]
# #     slide = presentation.slides.add_slide(slide_layout)
# #     title_box = slide.shapes.title
# #     content_box = slide.placeholders[1]
    
# #     title_box.text = title
# #     content_box.text = content

# # # Slide 1: Title Slide
# # add_slide(
# #     "Pest Identification using OpenCV",
# #     "Exploring Computer Vision Techniques for Effective Pest Detection",
# #     is_title_slide=True
# # )

# # # Slide 2: Introduction
# # add_slide(
# #     "Introduction",
# #     "• Pests are one of the major problems in agriculture, causing significant damage to crops.\n"
# #     "• Early detection of pests can help in reducing crop damage.\n"
# #     "• OpenCV, a popular computer vision library, can be utilized for pest detection using image processing techniques."
# # )

# # # Slide 3: Objectives
# # add_slide(
# #     "Objectives",
# #     "• Automate the process of identifying pests in images of crops.\n"
# #     "• Implement image processing techniques using OpenCV.\n"
# #     "• Provide a framework for integrating with real-time monitoring systems."
# # )

# # # Slide 4: Methodology
# # add_slide(
# #     "Methodology",
# #     "• Image Acquisition: Collect images from various sources, including real-time cameras.\n"
# #     "• Image Preprocessing: Convert images to grayscale, apply filters, and enhance features.\n"
# #     "• Pest Identification: Use contour detection, feature matching, and machine learning techniques."
# # )

# # # Slide 5: Image Preprocessing Techniques
# # generate_image("sample_pest.jpg", "output_pest.jpg")
# # add_slide(
# #     "Image Preprocessing",
# #     "• Techniques such as noise reduction, thresholding, and edge detection are crucial.\n"
# #     "• Example of thresholding applied to a pest image."
# # )

# # slide = presentation.slides[-1]
# # img_path = "output_pest.jpg"
# # slide.shapes.add_picture(img_path, Inches(2), Inches(2), width=Inches(4), height=Inches(3))

# # # Slide 6: Pest Identification with Contour Detection
# # add_slide(
# #     "Contour Detection",
# #     "• Contour detection helps in identifying the shape of pests in the image.\n"
# #     "• By identifying contours, we can isolate pests from the background."
# # )

# # # Slide 7: Feature Matching with ORB Detector
# # add_slide(
# #     "Feature Matching",
# #     "• ORB (Oriented FAST and Rotated BRIEF) is used for feature matching between images.\n"
# #     "• It helps in detecting pests based on their unique features."
# # )

# # # Slide 8: Machine Learning Approach
# # add_slide(
# #     "Machine Learning Approach",
# #     "• Machine learning algorithms like SVM, Random Forest, and CNNs can classify pests based on extracted features.\n"
# #     "• Training a model with a labeled dataset enhances detection accuracy."
# # )

# # # Slide 9: Results and Analysis
# # add_slide(
# #     "Results and Analysis",
# #     "• The implemented model successfully identifies common pests in test images.\n"
# #     "• Accuracy achieved ranges from 80% to 95%, depending on the quality of input images and the model used."
# # )

# # # Slide 10: Challenges
# # add_slide(
# #     "Challenges",
# #     "• Variation in lighting conditions can affect detection accuracy.\n"
# #     "• Overlapping pests and occlusions make identification difficult.\n"
# #     "• The need for a large, annotated dataset for training models."
# # )

# # # Slide 11: Conclusion and Future Work
# # add_slide(
# #     "Conclusion and Future Work",
# #     "• OpenCV offers a powerful toolkit for developing pest identification systems.\n"
# #     "• Future work can focus on integrating deep learning models for improved accuracy.\n"
# #     "• Real-time monitoring systems can help in early pest detection and control."
# # )

# # # Save the presentation
# # presentation.save("Pest_Identification_OpenCV_Presentation.pptx")
# # print("Presentation created successfully!")



# from pptx import Presentation
# from PIL import Image
# import io

# # Open the PowerPoint file
# ppt_path = 'vjit logo.pptx'
# presentation = Presentation(ppt_path)

# # Specify the slide index (0 for the first slide)
# slide_index = 0
# slide = presentation.slides[slide_index]

# # Save the slide as an image
# image_stream = io.BytesIO()
# slide.shapes[0].element.blob.save(image_stream)

# # Convert to PNG
# image = Image.open(image_stream)
# image.save('slide_image.png', 'PNG')

# print("Slide converted to PNG successfully!")







# from PIL import Image
# from transformers import BlipProcessor, BlipForConditionalGeneration

# def generate_narrative(image_path):
#     # Load the BLIP model and processor
#     processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
#     model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

#     # Load the image
#     image = Image.open(r"C:\Users\kanak\Pictures\red-apple-ground-with-leaves-ground_670382-18704 (1).jpg").convert("RGB")

#     # Process the image and generate caption
#     inputs = processor(images=image, return_tensors="pt")
#     outputs = model.generate(**inputs)
#     caption = processor.decode(outputs[0], skip_special_tokens=True)
    
#     return caption

# if __name__ == "__main__":
#     image_path = input("Enter the path to the image: ")
#     try:
#         narrative = generate_narrative(image_path)
#         print("\nGenerated Narrative:")
#         print(narrative)
#     except Exception as e:
#         print(f"Error: {e}")



from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import pyttsx3

def generate_narrative(image_path):
    # Load the BLIP model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Load the image
    image = Image.open(image_path).convert("RGB")

    # Process the image and generate caption
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    return caption

def speak_text(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set speech properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    try:
        # Generate narrative
        narrative = generate_narrative(image_path)
        print("\nGenerated Narrative:")
        print(narrative)

        # Speak the narrative directly
        speak_text(narrative)

    except Exception as e:
        print(f"Error: {e}")

