import streamlit as st
import cv2
import tempfile
import numpy as np
from pathlib import Path
from yt_dlp import YoutubeDL
from streamlit_webrtc import webrtc_streamer, WebRtcMode


class GDP:
    def __init__(self):
        self.cap=None


    def app(self):
        st.title('Stream contenta josko 0_0')

        source_option = st.selectbox(
            "Sourcik vyberi pacan",
            ("Pokophone","Youtube Link","Local Drive","Web-Camera","RTSP")
        )

        video_url=None
        img_file=None

        if source_option == "Pokophone":
            img_file = st.camera_input("Take a photorrrs")

        elif source_option == "Youtube Link":
            youtube_url = st.text_input("Put in a link")
            if youtube_url:
                with st.spinner("Gruzitsya..."):
                    try:
                        ydl_opts = {"format": "best[ext=mp4]/best", "noplaylist":True}
                        with YoutubeDL(ydl_opts) as ydl:
                            info_dict = ydl.extract_info(youtube_url,download=False)
                            video_url = info_dict.get("url", None)
                    except Exception as e:
                        st.error(f"Smth is wrong: {e}")

                if video_url:
                    st.video(video_url)

        elif source_option == "Local Drive":
            video_file = st.file_uploader("Upload vidos", type=["mp4","avi","mov"])
            if video_file:

                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=Path(video_file.name).suffix)
                temp_file.write(video_file.read())
                video_url = temp_file.name
                st.video(video_url)

        elif source_option == "Web-Camera":
            st.write("Webka gruzitsya...")
            webrtc_streamer(key="webcam",mode=WebRtcMode.SENDRECV)

        elif source_option == "RTSP":
            rtsp_url = st.text_input("Put in a rtsp link")
            if rtsp_url:
                video_url = rtsp_url

        run_button = st.button("Oh heeeeell naah")
        frame_place = st.empty()

        if source_option == "Pokophone" and img_file is not None:
            file_bytes=np.asarray(bytearray(img_file.read()), dtype = np.uint8)
            frame = cv2.imdecode(file_bytes,1)
            st.image(frame, channels="BGR")

        elif run_button and video_url is not None and source_option in ["Local Drive", "RTSP"]:
            self.cap = cv2.VideoCapture(video_url)


            if not self.cap.isOpened():
                st.error("Error")
            else:


                stop_button = st.button("Stop!!!")

                while self.cap.isOpened() and not stop_button:
                    ret, frame = self.cap.read()
                    if not ret:
                        st.write("Idi naher")
                        break

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_place.image(frame, channels="RGB")

                    if stop_button:
                        break

                self.cap.release()
                cv2.destroyAllWindows()

app = GDP()
app.app()