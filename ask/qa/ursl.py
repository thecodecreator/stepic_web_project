urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^login/', user_login, name='login'),
    url(r'^signup/', user_signup, name='signup'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', test, name='new'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
]
