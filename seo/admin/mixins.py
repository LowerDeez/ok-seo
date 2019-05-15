from django import forms
from django.db import models

from .utils import get_html_field_widget

__all__ = (
    'AdminRichTextFieldMixin',
)


class AdminRichTextFieldMixin:
    """
    Convert given text fields to rich text fields
    """
    rich_text_fields = [
        'seo_text'
    ]

    def get_rich_text_fields(self):
        return self.rich_text_fields

    def formfield_for_dbfield(self, db_field, **kwargs):
        if self.is_text_field(db_field):
            rich_text_fields = self.get_rich_text_fields()
            if rich_text_fields and db_field.name in set(rich_text_fields):
                return db_field.formfield(widget=get_html_field_widget())
            return db_field.formfield(widget=forms.Textarea())
        return super().formfield_for_dbfield(db_field, **kwargs)

    @staticmethod
    def is_text_field(field):
        return isinstance(field, models.TextField)
