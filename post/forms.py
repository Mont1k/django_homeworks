from django import forms

from post.models import Category, Review


class ProductCreateForm(forms.Form):
    name = forms.CharField(max_length=200)
    characteristic = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    price = forms.FloatField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="------", required=False,
                                      initial=None)

    def clean_content(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if len(content) < 30:
            raise forms.ValidationError("Content to short!")
        if not content:
            raise forms.ValidationError("Content is rewuired!")

        return cleaned_data


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'text']
        widgets = {'text': forms.Textarea(), }
