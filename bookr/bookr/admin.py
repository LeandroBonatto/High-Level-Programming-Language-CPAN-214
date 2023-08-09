from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    site_title = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'
    logout_template = 'logged_out.html'
