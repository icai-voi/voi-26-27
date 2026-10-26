<a href="https://x.com/nearcyan/status/1706914605262684394">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/object-tracking-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="assets/object-tracking-light.png">
    <img alt="Lab Session Image" src="assets/object-tracking-light.png">
  </picture>
</a>


**Welcome to the 5th lab session of Computer *Vision I* at Comillas ICAI**. Here, you will find all the necessary files to complete this session. 💻📷


## Resources

This laboratory session contains the following:

- 📄 **``CVI_lab_5.pdf``**: A ``PDF`` guide with instructions to complete the session (currently only available in Spanish).
- 💻 **Scripts**: Two ``.ipynb`` files (one per part: Object Detection - Background Subtraction, Optical Flow, Kalman Filter - and Bag of Words). The folder also includes helper scripts.
- 🎞️ **``data``**: A folder containing the videos to process.
- 📝 **``template``**: A folder with a ``latex`` template used to generate the guide. You can reuse it to write your report.
- 🧩 **``assets``**: Files to style or improve documentation.
- 📖 **``README``**: With links to motivate the session or to introduce the theory concepts.

The lab session folder is structured as follows:

```bash
.
├── CVI_Lab_4.pdf
├── src
│   └── partA-C.ipynb
│   └── partD.ipynb
├── data
│   └──partA-C
│       ├── slow_traffic_small.mp4
│       └── visiontraffic.avi
├── assets
├── template
└── README
```

## Get ready 🤓
If you're not enrolled or don't have access to the theory, or just want a refresher, check out the resources below before starting the lab.

- [Background Subtraction](https://www.youtube.com/watch?v=fn07iwCrvqQ)
- [Optical Flow](https://www.youtube.com/watch?v=lnXFcmLB7sM&list=PL2zRqk16wsdoYzrWStffqBAoUY8XdvatV)
- [Kalman Filter](https://thekalmanfilter.com/kalman-filter-explained-simply/)

<h2 align="center" style="margin-bottom: 0px;">Here we go: Lesson 4!</h2>
<h3 align="center" style="margin-top: 0px;">Object tracking</h3>
<p align="center">
  <img src="https://i.giphy.com/media/3o6MbmWIQi0dnHBXK8/giphy.gif" width="300" style="margin-bottom: 20px;" />
</p>