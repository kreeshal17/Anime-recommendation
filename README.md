# Anime Recommendation System

An intelligent anime recommendation system built using Machine Learning, Flask, and Pandas. The application recommends similar anime titles based on genres, ratings, episode count, popularity, and anime type.

## Features

* Anime similarity recommendations
* Genre-based feature extraction
* K-Means clustering for grouping similar anime
* Distance-based recommendation retrieval
* REST API built with Flask
* JSON response format
* CORS enabled for frontend integration

## Tech Stack

### Machine Learning

* Scikit-Learn
* K-Means Clustering
* Euclidean Distance

### Data Processing

* Pandas
* NumPy
* MultiLabelBinarizer
* StandardScaler

### Backend

* Flask
* Flask-CORS

## Dataset Features

The model uses:

* Genres
* Anime Type (TV, Movie, OVA, etc.)
* Rating
* Number of Episodes
* Member Count (Popularity)

## How It Works

### Data Preprocessing

* Missing values are handled.
* Genres are converted into numerical features using MultiLabelBinarizer.
* Anime types are one-hot encoded.
* Numerical features are standardized using StandardScaler.

### Model Training

* K-Means clustering groups similar anime into clusters.
* Each anime is assigned a cluster label.

### Recommendation Process

1. User provides an anime name.
2. The system identifies its cluster.
3. Similar anime from the same cluster are selected.
4. Euclidean distance is calculated.
5. Top 5 closest anime are returned.

## API Endpoint

### Recommend Anime

```http
POST /recommend
```

### Request Body

```json
{
  "anime": "Naruto"
}
```

### Success Response

```json
{
  "recommend": [
    {
      "name": "Bleach",
      "rating": 8.2,
      "episodes": 366
    }
  ]
}
```

### Error Response

```json
{
  "error": "not found",
  "recommend": []
}
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd anime-recommendation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Server will start on:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
anime-recommendation-system/
│
├── app.py
├── model.py
├── anime.csv
├── requirements.txt
└── README.md
```

## Future Improvements

* Content-based recommendation engine
* Collaborative filtering
* Hybrid recommendation model
* User authentication
* Personalized recommendations
* Recommendation confidence scores

## Author

Krishal Karna

## License

MIT License
