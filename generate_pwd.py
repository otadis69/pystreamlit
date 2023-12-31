import streamlit as st
import random
import string


def generate_password():
    length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    st.title("암호 생성기")

    if st.button("암호 생성"):
        password = generate_password()
        st.success(f"생성된 암호: {password}")


if __name__ == "__main__":
    main()
