// src
// https://docs.opencv.org/4.x/d9/df5/tutorial_js_intelligent_scissors.html

let src = cv.imread('./../resources/img/static/lenna.png');  // Load the image

// * This part is the main part of the code.
// * It is used to set the parameters for the tool and apply it to the image.
let tool = new cv.segmentation_IntelligentScissorsMB();  // Create an instance of the Intelligent Scissors tool
// The first parameter (32) represents the low threshold for the Canny edge detector.
// The second parameter (100) represents the high threshold for the Canny edge detector.
tool.setEdgeFeatureCannyParameters(32, 100);
tool.setGradientMagnitudeMaxLimit(200);  // Set the maximum limit for gradient magnitude
tool.applyImage(src);  // Apply the Intelligent Scissors tool to the loaded image

// * This part is used to build a path map starting from the clicked point.
let hasMap = false;  // Initialize a flag to track whether the path map has been built
// Create a reference to the 'canvasOutput' element
let canvas = document.getElementById('canvasOutput');  // Get a reference to the 'canvasOutput' element


// * This part is used to handle the mouse events.
canvas.addEventListener('click', e => {  // Add a click event listener to the 'canvasOutput' element
    let startX = e.offsetX, startY = e.offsetY;  // Get the X and Y coordinates of the click event
    console.log(startX, startY);
    if (startX < src.cols && startY < src.rows) {  // If the click event is within the image boundaries
        // console.time('buildMap');
        tool.buildMap(new cv.Point(startX, startY));  // Build a path map starting from the clicked point
        // console.timeEnd('buildMap');
        hasMap = true;  // Set the flag to indicate that the map has been built
    }
});

canvas.addEventListener('mousemove', e => {  // Add a mousemove event listener to the 'canvasOutput' element
    let x = e.offsetX, y = e.offsetY;  // Get the X and Y coordinates of the mousemove event
    let dst = src.clone();  // Create a clone of the source image
    if (hasMap && x >= 0 && x < src.cols && y >= 0 && y < src.rows) {  // If the mousemove event is within the image boundaries
        let contour = new cv.Mat();  // Create a Mat to store the contour
        tool.getContour(new cv.Point(x, y), contour);  // Get the contour for the current mouse position

        let contours = new cv.MatVector();  // Create a MatVector to hold the contours
        contours.push_back(contour);  // Add the contour to the MatVector

        let color = new cv.Scalar(0, 255, 0, 255);  // Define the color for drawing the contour (green in RGBA format)
        cv.polylines(dst, contours, false, color, 1, cv.LINE_8);  // Draw the contour on the clone of the source image
        contours.delete();  // Release memory allocated for contours
        contour.delete();  // Release memory allocated for contour
    }
    cv.imshow('canvasOutput', dst);  // Display the modified image in the 'canvasOutput' element
    dst.delete();  // Release memory allocated for the cloned image
});
canvas.addEventListener('dispose', e => {
    src.delete();  // Release memory allocated for the source image
    tool.delete();  // Release memory allocated for the tool
});
