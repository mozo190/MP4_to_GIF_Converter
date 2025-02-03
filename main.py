import os.path
import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox, QApplication
import moviepy
from moviepy.video.io.VideoFileClip import VideoFileClip


class MP4toGifConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MP4 to GIF Converter")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Select an MP4 file to convert to GIF")
        layout.addWidget(self.label)

        self.select_file_btn = QPushButton("Select File")
        self.select_file_btn.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_btn)

        self.convert_btn = QPushButton("Convert")
        self.convert_btn.setDisabled(True)
        self.convert_btn.clicked.connect(self.convert_to_gif)
        layout.addWidget(self.convert_btn)

        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select MP4 file", "", "MP4 Files (*.mp4)")
        if file_path:
            self.video_path = file_path
            self.label.setText(f"Chosen file: {os.path.basename(file_path)}")
            self.convert_btn.setDisabled(False)

    def convert_to_gif(self):
        if hasattr(self, "video_path"):
            gif_path = os.path.splitext(self.video_path)[0] + ".gif"

            self.label.setText("Converting...")
            self.repaint()

            clip = VideoFileClip(self.video_path)
            # clip = clip.subclip(0, 5) # Convert only the first 5 seconds
            clip.write_gif(gif_path)

            self.label.setText(f"Converted to GIF: {os.path.basename(gif_path)}")
            self.convert_btn.setDisabled(True)

            QMessageBox.information(self, "Success", "Conversion successful!")
        else:
            QMessageBox.warning(self, "Error", "No file selected!")


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MP4toGifConverter()
    win.show()
    sys.exit(app.exec())
