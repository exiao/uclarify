#helper function to update analyst summary
def add_new_review_to_analyst(analyst, review):
    if analyst.num_reviews == 0:
        analyst.num_reviews = 1
        analyst.average_rating = review.overall_rating
    else:
        new_avg = analyst.average_rating
        new_avg *= analyst.num_reviews
        new_avg += review.overall_rating

        analyst.num_reviews += 1
        new_avg /= analyst.num_reviews
        analyst.average_rating = new_avg
    analyst.recent_review = review
    analyst.save()
