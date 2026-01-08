import re
from collections import Counter
from datetime import datetime


def analyze_reviews(reviews):
    """
    Analyzes a set of reviews.

    Args:
        reviews: List of dictionaries with 'text', 'rating', 'date'
        Example: [
            {'text': 'Excellent product very good', 'rating': 5, 'date': '2024-01-15'},
            {'text': 'Good but could improve', 'rating': 3, 'date': '2024-02-20'}
        ]

    Returns:
        dict: {
            'average_rating': float,
            'month_with_most_reviews': str,
            'most_repeated_word': str
        }
    """

    # 1. Average rating
    ratings = [r["rating"] for r in reviews]
    average = sum(ratings) / len(ratings) if ratings else 0

    # 2. Month with most reviews
    months = [
        datetime.strptime(r["date"], "%Y-%m-%d").strftime("%Y-%m") for r in reviews
    ]
    month_with_most = Counter(months).most_common(1)[0][0] if months else None

    # 3. Most repeated word
    all_text = " ".join([r["text"].lower() for r in reviews])
    words = re.findall(r"\b\w+\b", all_text)

    # Filter common words (basic stopwords)
    stopwords = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for"}
    filtered_words = [w for w in words if w not in stopwords and len(w) > 2]

    most_repeated_word = (
        Counter(filtered_words).most_common(1)[0][0] if filtered_words else None
    )

    return {
        "average_rating": round(average, 4),
        "month_with_most_reviews": month_with_most,
        "most_repeated_word": most_repeated_word,
    }


# Usage example
example_reviews = [
    {"text": "Excellent product very good", "rating": 5, "date": "2024-01-15"},
    {"text": "Good but could improve", "rating": 3, "date": "2024-01-20"},
    {"text": "Product excellent", "rating": 5, "date": "2024-02-10"},
]

result = analyze_reviews(example_reviews)
print(result)
