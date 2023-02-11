from django.contrib import admin
from .models import Movie, Genre, MovieDisplayTimes

# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)


class MovieDisplayTimesInline(admin.TabularInline):
    model = MovieDisplayTimes
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "director")
    inlines = (MovieDisplayTimesInline,)
    exclude = ("rating",)

    def get_form(self, request, obj=None, **kwargs):
        # get base form object
        form = super(MovieAdmin, self).get_form(request, obj, **kwargs)

        # get the foreign key field I want to restrict
        genres = form.base_fields["genres"]

        # remove the green + by setting can_add_related to False on the widget
        genres.widget.can_add_related = False

        # return our now modified form.
        return form
