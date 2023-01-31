<h1>Preventive Maintenance Visual Inspection System</h1>

<p>This project is a visual inspection system using deep learning to assist technicians in identifying potential issues with equipment during preventive maintenance. The system is built with Industry 4.0 technologies such as IoT, big data analytics, and deep learning to predict and prevent equipment failure before it occurs.</p>

<h2>Directory Structure</h2>

<pre>
.
├── app
│   ├── bin
│   ├── lib
│   └── share
├── data
│   ├── csv
│   ├── data_flir
│   └── rgb
├── models
│   └── __pycache__
├── runs
│   └── detect
└── utils
    ├── aws
    ├── google_app_engine
    ├── __pycache__
    └── wandb_logging
</pre>

<h2>Installation</h2>

<p>To install the project, follow these steps:</p>

<ol>
  <li>Clone the repository to your local machine:<br>
  <pre>
  $ git clone https://github.com/[username]/preventive-maintenance-visual-inspection-system.git
  </pre></li>

  <li>Navigate to the project directory:<br>
  <pre>
  $ cd preventive-maintenance-visual-inspection-system
  </pre></li>

  <li>Download the dataset from <a href="https://drive.google.com/file/d/1BzfybGG1swTHTa-LB7nqrLLTRcnjJ-WE/view?usp=sharing">this link</a></li>

  <li>Place the dataset in the `data` directory.</li>

  <li>Install the required packages using pip:<br>
  <pre>
  $ pip install -r requirements.txt
  </pre></li>
</ol>

<h2>Running the App</h2>

<p>To run the app, use the following command:<br>
<pre>
$ python app_graph.py
</pre></p>

<h2>Note</h2>

<p>The code assumes the dataset is in a specific format and naming convention, so be sure to follow the instructions in the code comments when preparing the dataset.</p>
