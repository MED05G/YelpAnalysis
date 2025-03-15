#Business & Friend Recommendation System

##📌 Overview

This project leverages big data processing and AI-driven recommendations to build an advanced business and friend recommendation system. The system uses collaborative filtering, NLP, and graph-based techniques, integrated with ChatGPT API, to provide accurate and personalized recommendations.

##🚀 Features

Requirement 1: Data Analysis and Visualization

###I. Business Analysis

Identify the top merchants, cities, and states based on business frequency and ratings.

Analyze restaurant types and review distribution.

Extract insights on popular categories and businesses receiving the most five-star reviews.

###II. User Analysis

Track user growth and engagement.

Identify top reviewers and most influential users.

Compare elite users vs. regular users.

###III. Review Analysis

Count and rank reviews per year.

Extract the top words in positive and negative reviews.

Perform word cloud analysis and word association graphing.

###IV. Rating & Check-in Analysis

Analyze rating distribution and trends.

Track check-ins by year, hour, and city.

###V. Comprehensive Insights

Rank top merchants per city based on ratings, check-ins, and reviews.

Requirement 2: Big Data Application Development

###I. Friend Recommendation System

Collaborative Filtering-Based Recommendations

Compute user similarity (cosine, Pearson correlation).

Suggest friends based on common interests.

Interest-Based (Content-Based Filtering)

Extract user interests from reviews & bios using ChatGPT API.

Compute semantic similarity to recommend friends.

Graph-Based Social Network Recommendation

Build a User-Business-Review Graph and apply GNNs/PageRank.

###II. Business Recommendation System

User Profile-Based Recommendation

Use SVD, ALS, DNN, AutoEncoders to predict preferences.

NLP-Based Recommendations

Extract key business terms and sentiments from reviews using ChatGPT API.

Location-Based Recommendations

Recommend businesses using Haversine formula & KNN.

###III. ChatGPT API for Smart Recommendations

Personalized Chat-Based Search (e.g., "Recommend a Japanese restaurant near me.")

Business Insights (e.g., "Your restaurant has low weekend traffic. Offer discounts.")

##⚡ Tech Stack

Big Data Processing: PySpark, SQL, Zeppelin

Machine Learning: Scikit-Learn, Surprise, Deep Learning Models

NLP & ChatGPT: OpenAI API, Text Processing

Recommendation Algorithms: Collaborative Filtering (SVD, ALS), Content-Based, Graph-Based (GNNs, PageRank)

Geospatial Analysis: Haversine, KNN

Web Framework: Streamlit (for UI)