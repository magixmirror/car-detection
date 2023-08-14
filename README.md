# Car Parking Space Detection App

![ezgif com-optimize (2)](https://github.com/zsoltgeier/Car-parking-space-finder/assets/116493077/0975a427-bb62-48e4-859f-8efbfa3876af)


This Python app allows you to detect and monitor free or occupied car parking spaces from a top-view video footage of a parking lot. The app uses computer vision techniques to process the video and identify the occupancy status of each parking space in real-time.

## Features

- **Parking Space Detection**: The app allows you to mark the positions of parking spaces in the parking lot using a graphical user interface. You can add or remove parking spaces as needed.

- **Real-time Occupancy Status**: The app provides real-time occupancy status for each parking space. It displays a rectangle around each space and shows whether it is "Occupied" or "Free."

## Requirements

To run the app, you need the following:

- Python 3.x
- OpenCV library
- Numpy library
- cvzone library

You can install the required libraries using `pip`:

```bash
pip install opencv-python
pip install numpy
pip install cvzone
```

## Usage

1. **Clone the Repository**:
   - Clone this repository to your local machine using the following command:

     ```bash
     git clone https://github.com/zsoltgeier/car-parking-space-finder.git
     ```

2. **Replacing the demo video footage**:
   - Replace the default video footage (`carPark.mp4`) with your own video footage of the parking lot. Ensure that the video has a top-down view and captures the parking spaces clearly.
   - Replace the default screenshot (`carParkImg.png`) with a screenshot from your video footage. This screenshot will be used for marking the positions of parking spaces accurately.

   **Note**: Depending on the lighting conditions, camera quality, and parking lot layout of your specific video footage, you might need to tweak the parameters of the image processing functions in `main.py` for optimal results. These parameters may include threshold values, blur kernels, and more.


3. **Mark Parking Spaces**:
   - Run the `ParkingSpacePicker.py` script to mark the positions of parking spaces in the parking lot. Click on the image to add a parking space and right-click to remove a space.

     ```bash
     python ParkingSpacePicker.py
     ```

4. **View Real-time Occupancy**:
   - Once you have marked the parking spaces, run the `main.py` script to process the video footage and view the real-time occupancy status of each parking space.

     ```bash
     python main.py
     ```
