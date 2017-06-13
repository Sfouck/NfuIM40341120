from lib.recommender_systems import *


if __name__ == "__main__":

    print "Popular Interests"
    print popular_interests
    print

    print "------------------------------"
    print "Most Popular New Interests"
    print "already like:", ["Python", "statistics", "probability", "HBase"]
    print most_popular_new_interests(["Python", "statistics", "probability", "HBase"])
    print "------------------------------"


    print "Most Popular New Interests"
    print "already like:", ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"]
    print most_popular_new_interests(["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"])
    print
    print "already like:", ["R", "Python", "statistics", "regression", "probability"]
    print most_popular_new_interests(["R", "Python", "statistics", "regression", "probability"])
    print

    print "Unique Interests"
    print unique_interests
    print

    print "User based similarity"
    print "most similar to 15"
    print most_similar_users_to(15)

    print "Suggestions for 15"
    print user_based_suggestions(15)
    print

    print "Item based similarity"
    print "most similar to 'Big Data'"
    print most_similar_interests_to(0)
    print

    print "suggestions for user 5"
    print item_based_suggestions(5)