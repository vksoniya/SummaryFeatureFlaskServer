# Summary Feature Server 
A server that servers the summarization feature built using python and Flask

## Project
This server is built under the WILPS project under the Language Technology Group at Universitat Hamburg. The server performs the summarization of meeting conversation, while the meeting is happening. This server can be used as a standalone service, under the WILPS project, this server is integrated to the [BigBlueButton](https://github.com/vksoniya/bigbluebutton.git) (BBB) project. The BBB application is modified to integrate this feature. 

## Description
This feature server creates meeting summaries as follows:
    Extracts the transcripts from the ASR in a per-set time interval
    Summarizes the extracted meeting conversation
    The Summary is available for the meeting user to view while the conference is on-going

## Table of contents

* [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Transformer Model](#transformer-model)
* [Using Feature Server](#using-feature-server)
* [Integration to BBB](#integration-to-bbb)
* [Testing Feature Server](#testing-feature-server)
* [Using as Standalone Server](#standalone-server)
* [License](#license)


## Installation
This section explaines how this feature server can be installed and also configure all the components necessary for running this server as a web component using Flask. 


## Prerequisites
An Automatic Speech Recognizer (ASR) component is required for this model to create summaries. It could be any open source ASR that creates a transcript of ongoing voice streams. 
Under the WILPS project, the [Kaldi](https://kaldi-asr.org/) ASR is integrated and publishes the transcripts to the Redis PubSub message broker. 

System Requirements (Recommended):
The following are the minimum recommendations:
4 core CPU / 8 GB RAM / 25 GB of SSD storage for the production server 
Software Requirements
OS: Ubuntu 18.x
Free ports: 4047 (Bigbluebutton HTML5 client) & 7030 (Flask Server)
Python 3.6.9 (check version)
```sh
python3 --version
```

pip3 (check version)
```sh
pip3 --version
```

## Transformer Model
The model used here is a pretrained BART Model which is a variant of Bidirectional Encoder Representations from Transformers (BERT) 

The Bart model was proposed by Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov and Luke Zettlemoyer on 29 Oct, 2019. According to the abstract:

Bart uses a standard seq2seq/machine translation architecture with a bidirectional encoder (like BERT) and a left-to-right decoder (like GPT).
The pretraining task involves randomly shuffling the order of the original sentences and a novel in-filling scheme, where spans of text are replaced with a single mask token.
BART is particularly effective when fine tuned for text generation but also works well for comprehension tasks. It matches the performance of RoBERTa with comparable training resources on GLUE and SQuAD, achieves new state-of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks, with gains of up to 6 ROUGE.

### Installation
In this section, the necessary installations and cloning will be done for running the Summarizer Server
Important: It is recommended to install and run these components in python environement, to avoid conflict in dependencies and versions of libraries.

1. Create a project folder and create python environment in the project folder
```sh
mkdir <your_project_folder>
cd <your_project_folder>
python3 -m venv <your_env_name>
```

2. Clone this Git Repo into your project folder
```sh
git clone https://github.com/vksoniya/SummaryFeatureFlaskServer.git
```

3. Activate your environment and install requirements 
```sh
source <your_env_name>/bin/activate
pip install -r requirements.txt
```

## Using Feature Server

1. Once the above steps are completed, you are ready to use the server. Under your active environement, run the server as follows:
```sh
python3 summarizer_model.py
```

A few things to keep in mind, since this server is integrated to the BBB server, there are a few dependencies that requires to be availabe for this model to work:
1. A redis pubsub message broker where the meeting information is available
2. A transcription file for the respective meeting under /MeetingTranscriptData/<conf_id>_transcript.txt

2. A second component, which servers as the front-end for BBB HTML5 client is the Flask Server. Open a new terminal and activate the same python virtual environement. Run the flask server as follows: (default port used: 7030) 
```sh
python3 summary_server.py
```

To run this as a standalone component, refer section [Using as Standalone Server](#standalone-server)

## Integration to BBB
This feature is implemented an adapted to integrate to the BigBlueButton video conferencing tool. Check the config_bbb.txt for further instructions

## Testing Feature Server
The following steps require to be followed for testing the feature server

1. Terminal 1: Ensure that summarizer_model.py is running
2. Terminal 2: Ensure that the flask server summary_server.py is running at 'http://127.0.0.1:7030/' is running

Seperate Terminals are recommended so that the respective logs can be viewed.

Start a new meeting in BBB. The HTML5 client will be visible as follows (with the Summarize button)
<image>

While the meeting is going in progress, click the 'Summarize' button to see the following (please give a few seconds as the summarization is online and is configured to have a few seconds delay):
<image>


## Using as Standalone Server
Follow the instructions in config_standalone.txt to use this feature as a standalone component

## License

This project is open source for everyone. 

#Create a pdf download for the summary post meeting being over <-
# check for meeting end flag in redis pubsub
