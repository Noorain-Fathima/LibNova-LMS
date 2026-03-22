from django.contrib import admin
from django.contrib.auth.models import User
from .models import Book,StudentExtra,IssuedBook

# Book admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','isbn','author','category')

admin.site.register(Book, BookAdmin)


# Student admin
class StudentExtraAdmin(admin.ModelAdmin):
    list_display = ('user','enrollment','branch')
    search_fields = ('user__username','enrollment','branch')

admin.site.register(StudentExtra, StudentExtraAdmin)


# Issued book admin
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('enrollment','isbn','issuedate','expirydate')

admin.site.register(IssuedBook, IssuedBookAdmin)


