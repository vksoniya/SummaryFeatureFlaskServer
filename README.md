# Summary Feature Server
A flask server that servers the summarization feature. 

## Summarizer Model
The model used here is a pretrained BART Model which is a variant of Bidirectional Encoder Representations from Transformers (BERT) 

The Bart model was proposed by Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov and Luke Zettlemoyer on 29 Oct, 2019. According to the abstract,

    Bart uses a standard seq2seq/machine translation architecture with a bidirectional encoder (like BERT) and a left-to-right decoder (like GPT).

    The pretraining task involves randomly shuffling the order of the original sentences and a novel in-filling scheme, where spans of text are replaced with a single mask token.

    BART is particularly effective when fine tuned for text generation but also works well for comprehension tasks. It matches the performance of RoBERTa with comparable training resources on GLUE and SQuAD, achieves new state-of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks, with gains of up to 6 ROUGE.


## Prerequisite
An Automatic Speech Recognizer (ASR) component is required for this model to create summaries

## Description
This feature server creates meeting summaries as follows:
    Extracts the transcripts from the ASR in a per-set time interval
    Summarizes the extracted meeting conversation
    The Summary is available for the meeting user to view while the conference is on-going

## Integration to BigBlueButton
This feature is implemented an adapted to integrate to the BigBlueButton video conferencing tool 

