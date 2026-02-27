from django.contrib import admin
from .models import Question, Choice


# ---------- Admin Site Titles ----------
admin.site.site_header = "Polls Administration"
admin.site.site_title = "Polls Admin Portal"
admin.site.index_title = "Welcome to Polls Admin"


# ---------- Inline Choices ----------
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# ---------- Question Admin ----------
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    date_hierarchy = 'pub_date'
    inlines = [ChoiceInline]

    # Attach custom admin CSS
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


# ---------- Choice Admin ----------
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
    list_filter = ('question',)
    search_fields = ('choice_text',)

    # Attach custom admin CSS
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }