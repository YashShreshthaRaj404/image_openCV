# OpenCV 
![logo](https://github.com/YashShreshthaRaj404/image_openCV/blob/main/OpenCV_Logo_with_text_svg_version.svg.png)
OpenCV (Open Source Computer Vision Library)
is a library of programming functions mainly for real-time computer vision.[2] Originally developed by Intel, it was later supported by Willow Garage, then Itseez (which was later acquired by Intel[3]). The library is cross-platform and licensed as free and open-source software under Apache License


# Installation and Usage
If you have previous/other manually installed (= not installed via pip) version of OpenCV installed (e.g. cv2 module in the root of Python's site-packages), remove it before installation to avoid conflicts.

Make sure that your pip version is up-to-date (19.3 is the minimum supported version): pip install --upgrade pip. Check version with pip -V. For example Linux distributions ship usually with very old pip versions which cause a lot of unexpected problems especially with the manylinux format.

Select the correct package for your environment:

There are four different packages (see options 1, 2, 3 and 4 below) and you should SELECT ONLY ONE OF THEM. Do not install multiple different packages in the same environment. There is no plugin architecture: all the packages use the same namespace (cv2). If you installed multiple different packages in the same environment, uninstall them all with pip uninstall and reinstall only one package.

a. Packages for standard desktop environments (Windows, macOS, almost any GNU/Linux distribution)

•Option 1 - Main modules package: 
```
pip install opencv-python
```
•Option 2 - Full package (contains both main modules and contrib/extra modules):
```
pip install opencv-contrib-python
```
(check contrib/extra modules listing from OpenCV documentation)
b. Packages for server (headless) environments (such as Docker, cloud environments etc.), no GUI library dependencies

These packages are smaller than the two other packages above because they do not contain any GUI functionality (not compiled with Qt / other GUI components). This means that the packages avoid a heavy dependency chain to X11 libraries and you will have for example smaller Docker images as a result. You should always use these packages if you do not use cv2.imshow et al. or you are using some other package (such as PyQt) than OpenCV to create your GUI.

•Option 3 - Headless main modules package: pip install opencv-python-headless
•Option 4 - Headless full package (contains both main modules and contrib/extra modules):
```
pip install opencv-contrib-python-headless
```
(check contrib/extra modules listing from OpenCV documentation)

### Import the package:

```
import cv2
```

All packages contain Haar cascade files. cv2.data.haarcascades can be used as a shortcut to the data folder. For example:

```
cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
```

### Read OpenCV documentation

Before opening a new issue, read the FAQ below and have a look at the other issues which are already open.




# CI build process
The project is structured like a normal Python package with a standard setup.py file. The build process for a single entry in the build matrices is as follows (see for example .github/workflows/build_wheels_linux.yml file):

In Linux and MacOS build: get OpenCV's optional C dependencies that we compile against

Checkout repository and submodules

OpenCV is included as submodule and the version is updated manually by maintainers when a new OpenCV release has been made
Contrib modules are also included as a submodule
Find OpenCV version from the sources

Build OpenCV

tests are disabled, otherwise build time increases too much
there are 4 build matrix entries for each build combination: with and without contrib modules, with and without GUI (headless)
Linux builds run in manylinux Docker containers (CentOS 5)
source distributions are separate entries in the build matrix
Rearrange OpenCV's build result, add our custom files and generate wheel

Linux and macOS wheels are transformed with auditwheel and delocate, correspondingly

### Install the generated wheel

Test that Python can import the library and run some sanity checks

Use twine to upload the generated wheel to PyPI (only in release builds)

Steps 1--4 are handled by pip wheel.

The build can be customized with environment variables. In addition to any variables that OpenCV's build accepts, we recognize:

```CI_BUILD```. Set to 1 to emulate the CI environment build behaviour. Used only in CI builds to force certain build flags on in setup.py. Do not use this unless you know what you are doing.
```ENABLE_CONTRIB``` and ENABLE_HEADLESS. Set to 1 to build the contrib and/or headless version
```ENABLE_JAVA```, Set to 1 to enable the Java client build. This is disabled by default.
```CMAKE_ARGS```. Additional arguments for OpenCV's CMake invocation. You can use this to make a custom build.