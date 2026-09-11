# 🕉️ Ganesha Metallic Gold Clean Animation

A Python-based **Computer Vision + Turtle Graphics** project that converts a Ganesha image into a clean **metallic-gold contour drawing** on a dark background.

The project uses **OpenCV** to process the image, detect contours and understand shape hierarchy, then uses **Python Turtle** to redraw those contours as a golden artwork.

---

## ✨ Features

* 🖼️ Loads a Ganesha image using OpenCV
* 📐 Automatically resizes the image while maintaining aspect ratio
* ⚫ Converts the image into grayscale
* 🔲 Applies binary thresholding
* 🔍 Detects image contours
* 🌳 Uses contour hierarchy to identify inner holes/details
* 🧹 Removes very small/noisy contours
* 🎨 Draws contours using Turtle Graphics
* 🥇 Uses metallic-gold colors for the artwork
* 🌑 Uses a dark background for better contrast
* 📍 Converts OpenCV coordinates into Turtle coordinates

---

## 🛠️ Technologies Used

* **Python 3**
* **OpenCV (`cv2`)** – Image processing and contour detection
* **NumPy** – Used by OpenCV internally / available for array operations
* **Turtle Graphics** – Drawing detected contours
* **OS Module** – Safe image-path handling

---

## 📂 Project Structure

```text
god/
│
├── ganesha.py
├── ganesh.jpg
└── README.md
```

Make sure `ganesh.jpg` is available in the same folder as `ganesha.py`.

---

## ⚙️ How It Works

The project follows this pipeline:

```text
Ganesha Image
      ↓
Load Image
      ↓
Resize Image
      ↓
Grayscale Conversion
      ↓
Binary Threshold
      ↓
Contour Detection
      ↓
Contour Hierarchy
      ↓
Noise Filtering
      ↓
Coordinate Conversion
      ↓
Turtle Drawing
      ↓
Golden Ganesha Artwork
```

---

## 🔍 Core Concepts

### 1. Image Loading

OpenCV loads the input image using:

```python
cv2.imread()
```

The program checks whether the image was successfully loaded before continuing.

### 2. Image Resizing

The image width is set to a fixed size while its height is calculated using the original aspect ratio.

This prevents the Ganesha image from becoming stretched or distorted.

### 3. Grayscale Conversion

The color image is converted into grayscale using:

```python
cv2.cvtColor()
```

This simplifies the image for further processing.

### 4. Thresholding

Binary thresholding converts the grayscale image into a black-and-white representation.

```python
cv2.threshold()
```

This makes it easier to identify boundaries.

### 5. Contour Detection

OpenCV detects the boundaries of visible shapes using:

```python
cv2.findContours()
```

These contours are later used as drawing paths.

### 6. Contour Hierarchy

The project uses:

```python
cv2.RETR_TREE
```

to understand relationships between outer shapes and inner shapes.

This helps identify areas such as holes or gaps inside the artwork.

### 7. Noise Filtering

Very small contours are ignored using contour area:

```python
cv2.contourArea()
```

This prevents unwanted tiny dots and noise from being drawn.

### 8. Coordinate Conversion

OpenCV and Turtle use different coordinate systems.

The program converts:

```text
OpenCV:
(0,0) → Top-Left

Turtle:
(0,0) → Center
```

The coordinates are adjusted so that the Ganesha artwork appears centered on the Turtle screen.

### 9. Turtle Drawing

Each contour is converted into a series of Turtle movements:

```python
pen.goto(x, y)
```

The contour is closed and filled using:

```python
pen.begin_fill()
pen.end_fill()
```

---

## 🎨 Color Scheme

The project uses two main colors:

```text
Gold Stroke → #D49B24
Gold Fill   → #F5C842
Background  → #181B22
```

The combination gives the artwork a simple **metallic-gold-on-dark** appearance.

---

## 🚀 Installation

### Step 1 — Install Python

Install Python 3 from the official Python website.

### Step 2 — Install OpenCV

Open terminal or PowerShell:

```bash
pip install opencv-python
```

NumPy is normally installed automatically with OpenCV, but it can also be installed separately:

```bash
pip install numpy
```

### Step 3 — Clone or Download the Project

Place the project files inside one folder:

```text
god/
├── ganesha.py
└── ganesh.jpg
```

---

## ▶️ Run the Project

Open terminal inside the project folder and run:

```bash
python ganesha.py
```

A Turtle window will open and the Ganesha contour artwork will be drawn.

---

## ⚠️ Common Error

### Image Not Loading

If you see:

```text
Error: Could not load 'ganesh.jpg'
```

check:

1. The image file exists.
2. The filename is exactly `ganesh.jpg`.
3. The image is inside the correct folder.
4. The file extension is correct.

Recommended path handling:

```python
base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, "ganesh.jpg")

img = cv2.imread(image_path)
```

This is more reliable than using a relative path such as:

```python
cv2.imread("god/ganesh.jpg")
```

---

## 💡 Why This Project?

This project demonstrates how **Computer Vision and Graphics** can work together.

Instead of simply displaying an image:

```text
Image → Display
```

the program performs:

```text
Image
  ↓
Computer Vision Processing
  ↓
Extract Shapes
  ↓
Understand Shape Hierarchy
  ↓
Recreate Artwork
```

This makes it a useful beginner project for understanding practical image processing.

---

## 🔮 Future Improvements

Possible improvements include:

* ✨ Smooth animation while drawing
* 🎨 Multiple gold/gradient effects
* 🖼️ Support for different input images
* ⚙️ User-controlled threshold values
* 🖱️ GUI for selecting images
* 📊 Real-time contour preview
* 💾 Save the final Turtle artwork
* 🚀 Optimize contour drawing for faster rendering

---

## 📚 Learning Outcomes

After completing this project, you can understand the basics of:

* Python file handling
* OpenCV image processing
* Grayscale images
* Binary thresholding
* Contour detection
* Contour hierarchy
* Noise filtering
* Coordinate systems
* Turtle graphics
* Combining multiple Python libraries in one project

---

## 👨‍💻 Project

**Project Name:** Ganesha Metallic Gold Clean Animation
**Language:** Python
**Domain:** Computer Vision + Graphics
**Level:** Beginner / Intermediate

---

## ⭐ Conclusion

This project transforms a normal Ganesha image into a **golden contour-based digital artwork** using Python.

It is a simple but practical demonstration of how **OpenCV can extract visual information from an image and Turtle Graphics can recreate that information as a drawing.**

If you found this project useful, consider ⭐ starring the repository.
