from django.contrib import admin
from django.db.models import Q

class CommentarySaeculo(admin.SimpleListFilter):
    title = 'commentary century'

    parameter_name = 'century'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('a13.3', 'Before 1250'),
            ('13.3-13.4', 'After 1250'),
            ('13', '13th cent. (1200-1299)'),
            ('14', '14th cent. (1300-1399)'),
            ('13-14', '13th-14th cent. (1200-1399)'),
            # ('13.3', '13.3 (1250-1274'),
            # ('13.4', '13.4 (1275-1299)'),
            # ('14.1', '14.1 (1300-1324)'),
            # ('14.2', '14.2 (1325-1349)'),
            # ('14.3', '14.3 (1350-1374)'),
            # ('14.4', '14.4 (1375-1399)'),
            ('p14.4', 'After 1400'),
            ('unknown', 'Unknown'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == '13':
            return queryset.filter(saeculo__contains='13')

        if self.value () == 'a13.3':
            return queryset.filter(
                Q(saeculo__contains='12') |
                Q(saeculo__contains='13.1') |
                Q(saeculo__contains='13.2')
            )

        if self.value () == '13.3-13.4':
            return queryset.filter(
                Q(seaculo__contains='13.3') |
                Q(saeculo__contains='13.4')
            )

        if self.value() == '13-14':
            return queryset.filter(
                Q(saeculo__contains='13') | Q(saeculo__contains='14')
            )

        if self.value() == '14':
            return queryset.filter(saeculo__contains='14')

        if self.value() == 'p14.4':
            return queryset.filter(
                Q(saeculo__contains='15') |
                Q(saeculo__contains='16')
            )

        if self.value() == 'unknown':
            return queryset.filter(saeculo__isnull=True)
