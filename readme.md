<h1 align="center">The Invisible Cloak Project 🧙‍♂️</h1>

<p align="center">
  A fun, real-time "invisibility cloak" effect created with Python and OpenCV.
</p>

---

### About This Project

This was a fun, quick-fire project I built to test my Python coding and debugging speed. The challenge I set for myself was to go from an idea to a working prototype in just a couple of minutes, making quick adjustments and using image masking techniques to get the effect just right.

The result is this cool "invisible cloak" effect using OpenCV, where a white object is used to make things behind it "disappear" by replacing it with a pre-recorded background!

### How It Works

The magic is created through a few simple computer vision steps:

1.  **Background Capture**: The script first takes a picture of the background without the "cloak" in it. This is our reference frame.
2.  **Real-time Video**: It then starts capturing video from your webcam.
3.  **Color Detection (Masking)**: For each new frame, it identifies all the pixels that match the color of the cloak (in this case, white). This creates a binary "mask".
4.  **Mask Refinement**: The initial mask can be noisy. Morphological operations (like opening and dilating) are used to clean it up, removing small spots and smoothing the edges.
5.  **Combining Frames**: The final image is created by combining two parts:
    *   The area of the background image that corresponds to where the cloak is.
    *   The area of the current video frame where the cloak is *not*.

When stitched together, it creates the illusion that you are seeing *through* the cloak to the background behind it.

### Getting Started

Follow these steps to get the project running on your local machine.

#### Prerequisites

*   Python 3.x
*   A webcam

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/invisible-cloak.git
    cd invisible-cloak
    ```
2.  **Install dependencies:**
    ```bash
    pip install opencv-python numpy
    ```

### Usage

1.  **Run the script:**
    ```bash
    python main.py
    ```
2.  The program will ask you to clear the scene. It will wait for 3 seconds and then capture the background.
3.  Once the background is captured, you can bring a white object (like a piece of paper or cloth) into the frame to act as your "invisible cloak".
4.  Press the **'q'** key to exit the program.

