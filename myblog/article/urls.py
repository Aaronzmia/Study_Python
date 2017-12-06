from django.conf.urls import include, url
from . import views
from . import list_views

urlpatterns = [
    url(r'^article-column/$', views.article_column, name='article_column'),
    url(r'^rename-column/$', views.rename_article_column, name='rename_article_column'),
    url(r'^del-column/$', views.del_article_column, name='del_article_column'),
    # 上传文章
    url(r'^article-post/$', views.article_post, name='article_post'),
    # 文章标题列表
    url(r'^article-list/$', views.article_list, name='article_list'),
    # 文章跳转
    url(r'^article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name="article_detail"),
    # 删除文章
    url(r'^del-article/$', views.del_article, name='del_article'),
    # 编辑文章
    url(r'^edit-article/(?P<article_id>\d+)/$', views.edit_article, name="edit_article"),
    # 新的文章标题列表
    url(r'^list-article-titles/$', list_views.article_titles, name="list_article_titles"),
    # 用户文章列表
    url(r'^list-article-titles/(?P<username>[-\w]+)/$', list_views.article_titles, name="author_articles"),
    # 新的文章跳转
    url(r'^list-article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', list_views.article_detail, name="list_article_detail"),
    # 点赞
    url(r'^like-article/$', list_views.like_article, name="like_article"),
    # 文章标签
    url(r'^article-tag/$', views.article_tag, name="article_tag"),
    url(r'^del-article-tag/$', views.del_article_tag, name="del_article_tag"),
]