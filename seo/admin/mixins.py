from django import forms
from django.apps import apps
from django.db import models

from .utils import get_html_field_widget

__all__ = (
    'AdminRichTextFieldMixin',
)


class AdminRichTextFieldMixin:
    """
    Convert given text fields to rich text fields
    """
    richtext_fields = [
        'top_text',
        'bottom_text'
    ]

    def get_richtext_fields(self):
        return self.richtext_fields

    def formfield_for_dbfield(self, db_field, **kwargs):
        if self.is_text_field(db_field):
            richtext_fields = self.get_richtext_fields()
            if richtext_fields and db_field.name in set(richtext_fields):
                return db_field.formfield(widget=get_html_field_widget())
            return db_field.formfield(widget=forms.Textarea())
        return super().formfield_for_dbfield(db_field, **kwargs)

    def is_text_field(self, field):
        return type(field) == models.TextField
