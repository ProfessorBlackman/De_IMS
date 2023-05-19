from django import forms


class SelectWithInput(forms.Select):
    input_class = 'inputbox'

    def __init__(self, attrs=None, choices=(), *args, **kwargs):
        super().__init__(attrs, choices, *args, **kwargs)
        self.input_attrs = {'class': self.input_class}

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        select_html = super().render(name, value, attrs=attrs, renderer=renderer)
        input_html = forms.TextInput(attrs=self.input_attrs).render(name, value, attrs=attrs, renderer=renderer)
        return f'{select_html}<br>{input_html}'
