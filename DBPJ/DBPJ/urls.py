"""DBPJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import view

urlpatterns = [
    url(r'^admin', admin.site.urls),

    # main_page
    url(r'^$', view.home),

    # users register & login & logout
    url(r'^register-form$', view.reg_form),
    url(r'^register$', view.reg),
    url(r'^login-form$', view.login_form),
    url(r'^get-login-name$', view.get_login_name),
    url(r'^logout$', view.logout),

    # manager login & logout
    url(r'^mlogin-form$', view.mlogin_form),
    url(r'^get-mlogin-name$', view.get_manager_name),
    url(r'^manager-page$', view.magager_page),
    url(r'^mlogout$', view.mlogout),

    # manager animation
    url(r'^m-animation$', view.m_all_animation),
    url(r'^modify-ani-state/(\d+)$', view.modify_animation_state),
    url(r'^m-add-animation-form$', view.manager_add_form),
    url(r'^m-add-animation$', view.manager_add_animation),

    # manager users
    url(r'^m-all-users$', view.m_all_users),
    url(r'^m-forbid1/(\d+)$', view.m_forbid1),
    url(r'^m-allow1/(\d+)$', view.m_allow1),
    url(r'^m-query-users$', view.m_query_name_form),
    url(r'^m-get-query-name$', view.m_get_query_name),
    url(r'^m-forbid2/(\d+)$', view.m_forbid2),
    url(r'^m-allow2/(\d+)$', view.m_allow2),
    url(r'^m-delete-comment1/(\d+)$', view.m_delete_comment1),

    # manager comment
    url(r'^m-all-comment$', view.m_all_comment),
    url(r'^m-delete-comment2/(\d+)$', view.m_delete_comment2),

    # users sub
    url(r'^user-sub$', view.mysub),
    url(r'^cancel-sub1/([^/]+)$', view.cancel_sub1),
    url(r'^user-sub-comment/(\d+)$', view.user_sub_comment),
    url(r'^get-user-comment$', view.get_user_comment),

    # users animation
    url(r'^user-all-animation$', view.user_all_animation),
    url(r'^cancel-sub2/(\d+)$', view.cancel_sub2),
    url(r'^add-sub1/([^/]+)$', view.add_sub1),
    url(r'^user-get-time/(\d+)/(\d+)$', view.user_get_time),
    url(r'^cancel-sub3/(\d+)$', view.cancel_sub3),
    url(r'^add-sub2/([^/]+)$', view.add_sub2),
    url(r'^user-get-query-ani$', view.get_query_animation),
    url(r'^cancel-sub4/(\d+)$', view.cancel_sub4),
    url(r'^add-sub3/([^/]+)$', view.add_sub3),
    url(r'^user-get-animation-comment/([^/]+)$', view.user_get_animation_comment),

    # user comment
    url(r'^user-all-comment$', view.user_all_comment),
    url(r'^user-my-comment$', view.user_my_comment),
    url(r'^user-animation-comment$', view.user_animation_comment),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
