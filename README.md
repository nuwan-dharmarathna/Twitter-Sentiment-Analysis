# Sentiment Analysis Project

## Description

This project is a sentiment analysis tool developed in Python, utilizing the NLTK library. It includes a small web application for predicting the sentiment (positive/negative) of user comments. The sentiment analysis model was trained on the Twitter sentiment analysis dataset, achieving an accuracy of 79%.

## Dataset

The sentiment analysis model was trained on the Twitter sentiment analysis dataset from kaggle.

link - [for the dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)

## Model Accuracy

The sentiment analysis model achieved an accuracy of 79% from Logestic Regression.

## Technologies Used

- Python
- NLTK (Natural Language Toolkit)

## Features

- Web application for user comment input - flask
- Sentiment prediction (positive/negative) using the trained model
- Displaying the prediction result to the user
- Batch sentiment prediction for Xquik CSV, JSON, and JSONL tweet exports

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m nltk.downloader stopwords
python app.py
```

## Xquik Batch Analysis

Export tweet results from [Xquik](https://xquik.com), then send the CSV, JSON,
or JSONL file to the batch endpoint:

```bash
curl --data-binary @tweets.json \
  --header "Content-Type: application/json" \
  http://127.0.0.1:5000/xquik-export
```

The response contains the normalized tweet, creation time, username, and
positive or negative prediction for every non-empty tweet.

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.

<img width="849" alt="Screenshot 2024-04-11 at 09 15 36" src="https://github.com/nuwan-dharmarathna/Twitter-Sentiment-Analysis/assets/137724808/f246c30d-a00f-4b40-83c4-b1ea22d09ef4">
