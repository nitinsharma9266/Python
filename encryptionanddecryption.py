import streamlit as st
from cryptography.fernet import Fernet

key='LKl_hrxH68tZKgjndzMku8eowKPyEO4zDGNICEpN77Q='
st.title('Massage Encrypt/Decrypt')

cipher=Fernet(key)
st.code(key)

msg=st.text_area("Enter Your massage ")

action=st.selectbox("coose optionn:",['Encrypt','Decrypt'])
if st.button("Submit"):
    if action=='Encrypt':
        encrypted=cipher.encrypt(msg.encode())
        st.code(encrypted.decode())
    else:
        decrypted=cipher.decrypt(msg.encode())
        st.code(decrypted.decode())

