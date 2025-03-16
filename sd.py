from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def generate_narrative(image_path):
    # Load the BLIP model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Load the image
    image = Image.open(r"C:\Users\kanak\Pictures\red-apple-ground-with-leaves-ground_670382-18704 (1).jpg").convert("RGB")

    # Process the image and generate caption
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    return caption

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    try:
        narrative = generate_narrative(image_path)
        print("\nGenerated Narrative:")
        print(narrative)
    except Exception as e:
        print(f"Error: {e}")