from django.contrib import admin
from django.urls import path, include
from HomePage import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home, name="home"),
    path('register', views.register, name="register"),
    path('login/',views.login_view,name="login"),
    path('booking_page', views.booking_page, name='booking'),
    path('detail/<str:selected_room_type>/', views.detail_page, name='detail'),
    path('billing_page/<int:booking_id>/', views.billing_page, name='billing_page'),
    path('confirm_booking/', views.confirm_room, name='confirm_booking'),
    path('service-selection/', views.service_selection, name='service_selection'),
    path('about', views.about, name='about'),
    path('contactus/',views.contact_us,name="contact_us"),
    path('afterlogin/',views.after_login,name="after_login"),
    #path('service-selection/<int:service_id>/', views.service_selection, name='service_detail'),
    path('book-service/<int:booking_id>/', views.book_service, name='book_service'),
    path('staff/', views.staff_viewer, name='Staff_Viewer'),  # Define the URL pattern for staff viewer
    path('dashboard/', views.dashboard, name="dashboard"),
    path('passwordChange/', views.passwordChange, name='passwordChange'),
    path('profileChange/', views.profileChange, name='profileChange'),
    path('logoutview', views.logoutview, name='logoutview'),
    path('regComplete', views.regComplete, name='regComplete'),
    path('checkout/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('incorrectDetails', views.incorrectDetails, name='incorrectDetails'),
    path('forgetPassword', views.forgetPassword, name="forgetPassword"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
