import streamlit as st
import cv2
import numpy as np
import pickle
import mediapipe as mp
import os

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
               10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
               19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'Hello', 27: 'Yes', 28: 'No',
               29: 'Thank you', 30: 'I Love You'}

st.title('Sign Language Detection')

# Sidebar
st.sidebar.title('Sign Language Detection')
st.sidebar.subheader('- Using ML Classifier & Streamlit')
st.sidebar.checkbox("Record Video", value=True)

# Get the path to the image file
image_path = os.path.join("images", "american_sign_language.jpg")

app_mode = st.sidebar.selectbox('Choose the App mode', ['About App', 'Sign Language to Text'])

# Get the path to the image file
image_path = os.path.join("images", "american_sign_language.jpg")

if app_mode == 'About App':
    st.title('Sign Language Detection Using MediaPipe with Streamlit GUI')
    st.markdown(
        'In this application we are using **MediaPipe** for detecting Sign Language. which convert to the American Sign Language . **StreamLit** is to create the Web Graphical User Interface (GUI) ')
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 400px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 400px;
            margin-left: -400px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.video('https://youtu.be/OIQskkX_DK0?si=teZ-CDrZ3NBKRcEX')
    st.markdown('''
                Also check out our Social Media
                - [YouTube](https://www.youtube.com)
                - [LinkedIn](https://www.linkedin.com)
                - [GitHub](https://github.com)
              If you are facing any issue while working feel free to mail

                - [Gmail](https://gmail.com)

                ''')
elif app_mode == 'Sign Language to Text':
    st.title('Sign Language to Text')

    use_webcam = st.sidebar.button('Use Webcam')
    record = st.sidebar.checkbox("Record Video")

    if record:
        st.checkbox("Recording", value=True)

    st.sidebar.markdown('---')
    st.markdown(' ## Output')

    stframe = st.empty()

    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    while True:
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,  # image to draw
                    hand_landmarks,  # model output
                    mp_hands.HAND_CONNECTIONS,  # hand connections
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10

            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            prediction = model.predict([np.asarray(data_aux)])

            predicted_character = labels_dict[int(prediction[0])]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)

        stframe.image(frame, channels='BGR', use_column_width=True)

        if not use_webcam:
            break

    cap.release()
# Display American Sign Language image below app mode section
if os.path.exists(image_path):
    st.sidebar.image(image_path, caption="American Sign Language", use_column_width=True)
else:
    st.sidebar.error("Error: Image file not found!")
