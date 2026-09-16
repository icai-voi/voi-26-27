<a href="https://x.com/nearcyan/status/1706914605262684394">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/cvi-icai-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="assets/cvi-icai-light.png">
    <img alt="Descripción de la imagen" src="assets/cvi-icai-light.png">
  </picture>
</a>


**Welcome to the repository for the *Computer Vision I* course at Comillas ICAI**. Here, you will find all the necessary files to complete the 4 lab sessions of the course, as well as a final lab project. 💻📷

The topics we will cover are:

* [ ] **Lab 1:** Introduction to OpenCV and Color Spaces 
* [ ] **Lab 2:** Camera Calibration
* [ ] **Lab 3:** Image processing and Features Extraction
* [ ] **Lab 4:** Features Extraction & Bag of Visual Words
* [ ] **Lab 5:** Motion Detection, and Object Tracking
* [ ] **Project:** Final Project

Each structured session is designed to be completed in 2 hours in the lab. The additional, non-guided questions we propose in the lab manual are intended as homework to be done outside of class time.

## Student Requirements

As a student, you are expected to have a basic knowledge of Python. Some exercises are self-contained, but having a basic understanding of the theoretical concepts behind each lab session is highly recommended. The course at ICAI is structured so that enrolled students will always have a theory lesson prior to the lab session.

For students outside ICAI or not enrolled in the course, we will provide relevant links for each lab session to help you get an introduction to the topic.

## Resources

An ``enviroment_$OSSystem$.yaml``file is provide to create a Conda environment with all required dependencies.

``$OSSystem$`` - win for windows; unix for Unix and macos for Mac.

💡 Tip: Create the Conda environment from this file:
```bash
conda env create -f environment.yml
conda activate <env-name>
```
If you update the file later, apply changes with:
```bash
conda env update -f environment.yml --prune
```

Each laboratory session contains the following:

- 📄 **Guide**: A ``PDF`` guide with instructions to complete the session (currently only available in Spanish).
- 💻 **Script**: a ``.ipynb`` or ``.py`` file to complete.
- 🎞️ **Data**: A folder containing images to process.
- 📝 **Template**: A folder with a ``latex`` template used to generate the guide. You can reuse it to write your report.
- 🧩 **Assets**: Files to style or improve documentation.
- 📖 **README**: With links to motivate the session or to introduce the theory concepts.

The lab sessions folder are structured as follows:

```bash
.
├── guide.pdf
├── src
│   ├── lab_session.ipynb
│   ├── lab_session.py
│   └── ...
├── data
│   ├── image1.png
│   ├── image2.png
│   └── ...
├── assets
├── template
└── README
```

## Expand
If you want to learn more, we recommend checking out the following resources:

- **[Book: *Programming Computer Vision with Python*](https://github.com/Ricky-Wilson/Programming-books/blob/master/PDF/OReilly.Programming.Computer.Vision.with.Python.Jun.2012.RETAIL.eBook-ELOHiM.pdf)**
- **[Tutorials: PyImageSearch](https://pyimagesearch.com/category/tutorials/)**.  *Old but gold*: If you want to learn classic computer vision, check out the older pages of the archive.



## Typos and Errors

If you spot a typo or notice a mistake, feel free to reach out or submit a pull request. We greatly appreciate your cooperation! 🤗

## Get in Touch

If you have suggestions for exercises or want to share your thoughts, feel free to contact us. Also, if you find this repository helpful, we would appreciate it if you could give it a star.


<h2 align="center">Let's start!</h2>
<p align="center">
  <img src="https://media.giphy.com/media/26BGIqWh2R1fi6JDa/giphy.gif" width="300" style="margin-bottom: 20px;" />
</p>
