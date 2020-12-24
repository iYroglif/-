from pytest_bdd import scenario, given, when, then


@given("I am a sports news user.")
def user(SportNews):
    subject = SportNews()


@when("I followed to football news")
def go_to_article(subject, FootballObserver):
    observer_a = FootballObserver()
    subject.follow(observer_a)


@then("I should be followed to football news")
def article_is_published(subject):
    assert subject.followed
