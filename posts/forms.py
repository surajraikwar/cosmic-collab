from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = (
            "message",
            "group",
            "post_type",
            "image",
            "observation_date",
            "location_description",
            "equipment_used",
        )
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
            'observation_date': forms.DateInput(attrs={'type': 'date'}),
            'equipment_used': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            # Limit group choices to groups the user is a member of
            self.fields["group"].queryset = models.Group.objects.filter(members=user)

        # Make image field not required by default in the form,
        # even though model allows blank=True, null=True.
        # Model's blank=True handles admin, form's required=False handles frontend form.
        self.fields['image'].required = False
        self.fields['observation_date'].required = False
        self.fields['location_description'].required = False
        self.fields['equipment_used'].required = False

        # Add Bootstrap classes for styling if needed, though Bootstrap 5 handles much of this
        # Example: self.fields['message'].widget.attrs.update({'class': 'form-control'})
        # This can also be done with django-bootstrap4 or a similar app, or directly in templates.
