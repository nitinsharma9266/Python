import streamlit as st
import os
from PIL import Image
from rembg import remove
import io

st.title ("Ai Background Remover ")

upload_file=st.file_uploader(" Upload an Image")
if upload_file:
    img=Image.open(upload_file)
    
    st.subheader("Original Image")
    
    st.image(img,use_container_width=True)
    
    if st.button("💥 Remove Background"):
        with st.spinner("Removing Background.... Please wait"):
            output=remove(img)
            
        st.subheader("Background Removed")
        st.image(output)
        
         

        # ✅ Download button fix
        img_bytes = io.BytesIO()
        output.save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()

        st.download_button(
            label="📥 Download Image",
            data=img_bytes,
            file_name="removed_background.png",
            mime="image/png"
        )
        


