# Summary Feature Server 
A server that servers the summarization feature built using python and Flask

## Project
This server is built under the WILPS project under the Language Technology Group at Universitat Hamburg. The server performs the summarization of meeting conversation, while the meeting is happening. This server can be used as a standalone service, under the WILPS project, this server is integrated to the [BigBlueButton] (https://github.com/vksoniya/bigbluebutton.git) (BBB) project. The BBB application is modified to integrate this feature. 

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
* [Testing Feature Server](#testing-feature-server)
* [Integration to BBB](#integration-to-bbb)
* [License](#license)


## Installation
This section explaines how this feature server can be installed and also configure all the components necessary for running this server as a web component using Flask. 


## Prerequisites
An Automatic Speech Recognizer (ASR) component is required for this model to create summaries. It could be any open source ASR that creates a transcript of ongoing voice streams. 
Under the WILPS project, the [Kaldi] (https://kaldi-asr.org/) ASR is integrated and publishes the transcripts to the Redis PubSub message broker. 

System Requirements (Recommended):
The following are the minimum recommendations:
4 core CPU / 8 GB RAM / 25 GB of SSD storage for the production server 
Software Requirements
OS: Ubuntu 18.x
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


## Using Feature Server
## Testing Feature Server

## Integration to BBB
This feature is implemented an adapted to integrate to the BigBlueButton video conferencing tool 

## License

This project is open source for everyone. 

