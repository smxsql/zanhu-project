from django.urls import path
from zanhu.articles import views
from django.views.decorators.cache import cache_page

app_name = "articles"
urlpatterns = [
    path("", views.ArticlesListView.as_view(), name = "list"),
    path("write-new-article/", views.ArticleCreateView.as_view(), name = "write_new"),
    path("drafts/", views.DraftListView.as_view(), name = "drafts"),
    # 把文章缓存5分钟
    path("<str:slug>/", cache_page(60 * 5)(views.ArticleDetailView.as_view()), name = "article"),
    path("edit/<int:pk>/", views.ArticleEditView.as_view(), name = "edit_article"),
]
