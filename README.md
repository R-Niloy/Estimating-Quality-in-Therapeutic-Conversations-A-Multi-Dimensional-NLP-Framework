# Therapeutic Conversation Quality Assessment Framework

A multi-dimensional Natural Language Processing (NLP) framework for analyzing and assessing the quality of therapeutic conversations.

## 🌟 Overview

This project presents a novel approach to evaluating therapeutic conversation quality using advanced NLP techniques and machine learning. Our framework analyzes key conversational dynamics to distinguish between high and low-quality therapeutic interactions, providing valuable insights for mental health professionals.

## 🔑 Key Features

- **Multi-dimensional Analysis**: Evaluates conversations across four key dimensions:
  - Conversation Analytics (turn-taking, word usage patterns)
  - Semantic Analysis (topic coherence and flow)
  - Sentiment Analysis (emotional context)
  - Question Detection (engagement patterns)

- **Advanced ML Classification**: Implements multiple classifiers including Random Forest, CatBoost, and SVM, achieving up to 97% accuracy with optimized parameters

- **Robust Data Processing**:
  - Handles imbalanced datasets using SMOTE-Tomek
  - Comprehensive outlier detection
  - Feature normalization and preprocessing

## System Arhcitecture
![System Architecture for NLP Framework](https://github.com/R-Niloy/Estimating-Quality-in-Therapeutic-Conversations-A-Multi-Dimensional-NLP-Framework/blob/main/src/additional%20resources/system_architecture.jpg)

## 📊 Performance Highlights

| Classifier | Accuracy | Precision | Recall | F1 Score | AUC Score |
|------------|----------|----------|---------|-----------|------------|
| SVM | 0.9717 | 0.9775 | 0.9667 | 0.9715 | 0.9874 |
| CatBoost | 0.9600 | 0.9606 | 0.9600 | 0.9600 | 0.9912 |
| Random Forest | 0.9533 | 0.9487 | 0.9600 | 0.9539 | 0.9893 |

## 🛠 Technical Implementation

### Feature Extraction Pipeline
1. **Conversation Analytics**:
   - Words per turn analysis
   - Turn-taking patterns
   - Statistical measures (std dev, skewness, kurtosis)

2. **Semantic Analysis**:
   - Utilizes multiple embedding models:
     - PromCSE
     - Sentence-BERT
     - SAKIL sentence similarity
   - Both overall and turn-order-aware analysis

3. **Sentiment Analysis**:
   - Twitter-roBERTa-base model
   - Sentiment transition tracking
   - Weighted certainty scores

4. **Question Detection**:
   - Syntactic pattern recognition
   - Bi-gram analysis
   - Speaker-specific question tracking

## 📦 Requirements

- Python 3.8+
- scikit-learn
- transformers
- torch
- pandas
- numpy
- catboost
- SVM
- Random Forest


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This research was supported by:
- Natural Sciences and Engineering Research Council of Canada (NSERC)
- New Frontiers in Research Fund
- LeaCros

## 📬 Contact

For questions and feedback, please contact [Niloy Roy](mailto:its.royniloy@gmail.com)
