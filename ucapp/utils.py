#helper function to update analyst summary
def add_new_review_to_analyst(analyst, review):
    if not analyst.num_reviews or analyst.num_reviews == 0:
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

#helper function to update analyst_firm summary
def add_new_review_to_analyst_firm(analyst_firm, review):
    if not analyst_firm.num_reviews or analyst_firm.num_reviews == 0:
        analyst_firm.num_reviews = 1
        analyst_firm.average_rating = review.overall_rating
    else:
        new_avg = analyst_firm.average_rating
        new_avg *= analyst_firm.num_reviews
        new_avg += review.overall_rating

        analyst_firm.num_reviews += 1
        new_avg /= analyst_firm.num_reviews
        analyst_firm.average_rating = new_avg
    analyst_firm.recent_review = review
    analyst_firm.save()