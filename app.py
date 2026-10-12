
import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import io

st.set_page_config(page_title="Chest X-ray Viewer")

st.title("Chest X-ray Image Viewer")
st.write("Upload and process chest X-ray images.")

uploaded_file = st.file_uploader(
    "Upload an X-ray image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Original X-ray")
    st.image(image, use_container_width=True)

    grayscale = st.checkbox("Convert to grayscale")
    brightness = st.slider("Brightness", 0.5, 2.0, 1.0)
    contrast = st.slider("Contrast", 0.5, 3.0, 1.0)

    processed = image

    if grayscale:
        processed = ImageOps.grayscale(processed)

    processed = ImageEnhance.Brightness(
        processed
    ).enhance(brightness)

    processed = ImageEnhance.Contrast(
        processed
    ).enhance(contrast)

    st.subheader("Processed X-ray")
    st.image(processed, use_container_width=True)

    output = io.BytesIO()
    processed.save(output, format="PNG")

    st.download_button(
        "Download Processed Image",
        data=output.getvalue(),
        file_name="processed_xray.png",
        mime="image/png"
    )

st.caption("Educational use only. Not a diagnostic tool.")
