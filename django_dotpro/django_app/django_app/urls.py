
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from decorator_include import decorator_include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', decorator_include(login_required, include('memo_app.urls'))),
    path('accounts/', include('allauth.urls')),
    # path('accounts/logout/', include('allauth.account.views.LogoutView'), name='logout'),
]
