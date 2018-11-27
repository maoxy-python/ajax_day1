from django.urls import path
from django.views.generic import TemplateView

from ajax_app import views

urlpatterns = [
    path("hello/",views.handle_ajax,name="hello"),
    path("page/",TemplateView.as_view(template_name="ajax_app/hello_world.html")),
    path("page2/", TemplateView.as_view(template_name="ajax_app/hello_world_post.html")),
    path("username/page/", TemplateView.as_view(template_name="ajax_app/username.html")),
    path("username/logic/",views.handle_username,name="username"),
    path("compare/", TemplateView.as_view(template_name="ajax_app/compare.html")),
]