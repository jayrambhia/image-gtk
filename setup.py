from setuptools import setup, find_packages

setup(name="imagegtk",
    version = 0.1,
    download_url = "https://github.com/jayrambhia/imagegtk/downloads/tarball/master",
    description = "Gtk GUI for OpenCV and SimpleCV",
    keywords = "opencv, cv, simplecv, opentld, gtk, GUI",
    author = "Jay Rambhia",
    author_email = "jayrambhia777@gmail.com",
    license = 'BSD',
    packages = find_packages(),
    requires = ["gtk","pygtk"]
    )
