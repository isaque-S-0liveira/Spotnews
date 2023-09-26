from django import forms
from news.models.news_model import News, Users, Categories


class CreateCategoriesForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"type": "text"}),
        label="Nome",
    )


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["title"].widget = forms.TextInput(
            attrs={"type": "text", "name": "title"}
        )
        self.fields["content"].label = "Conteúdo"
        self.fields["content"].widget = forms.Textarea(
            attrs={"name": "content"}
        )
        self.fields["author"].label = "Autoria"
        self.fields["author"].widget = forms.Select(
            attrs={"name": "author"},
            choices=[(user.id, user.name) for user in Users.objects.all()],
        )
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )
        self.fields["image"].label = "URL da Imagem"
        self.fields["image"].widget = forms.FileInput(attrs={"name": "image"})

        self.fields["categories"].widget = forms.CheckboxSelectMultiple(
            choices=[
                (category.id, category.name)
                for category in Categories.objects.all()
            ],
        )
