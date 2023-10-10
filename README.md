<h1 align="center">
    <img src=".\resources\img\static\philosophers-stone.png" alt="Digital Strategy" width="128">
    <div align="center">Image Alchemy</div>
</h1>

Elevate your imagery with ImageAlchemy, a cutting-edge computer vision project designed to seamlessly metamorphose your photos into captivating works of art.
Also **keep your entire editing journey** neatly documented in an automatic editing history for your convenience and creative exploration.

## Setup
The current python version is `3.11.*`. It is recommended to use the same version to avoid any issues.  

The project is still on development, so the **setup is not automated yet**.

- Create and activate the virtual environment
```bash
# Using venv
python -m venv .venv  # create the environment
source .venv/bin/activate  # activate on linux
.venv\Scripts\activate  # activate on windows
pip install -r requirements.txt # install dependencies

# Using mamba (conda)
mamba env create -f environment.yml  # create the environment
conda activate cv  # activate the environment
```

- Run the project from the root dir (intelligent_scissors/)
```bash
python src/main.py  # run the main file
```

## Test the project
To be sure that everything is working as expected, run the tests.
```bash
python -m unittest discover -s src/tests -p test_*.py  # run all tests in src/tests
```


## References
- [Interactive IS (cv)](https://docs.opencv.org/4.x/d9/df5/tutorial_js_intelligent_scissors.html) Interactive Intelligent Scissors using OpenCV
- [Intelligent Scissors for Image Composition](./log/IS%20for%20image%20composition.pdf) (Original paper)
- [Interactive Segmentation with Intelligent Scissors](./log/interactive%20segmentation%20with%20IS.pdf)  (Extended paper)

## [License](./LICENSE)

This project is licensed under the [MIT License](./LICENSE).

But it also uses [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) and [OpenCV](https://opencv.org/) which have their own licenses.
- [PyQt6 License](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html#license) (GPLv3 License)
- [OpenCV License](https://opencv.org/license/) ([Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/))