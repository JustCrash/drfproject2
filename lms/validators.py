from rest_framework.exceptions import ValidationError


class LinkValidator:

    def __init__(self, filed):
        self.filed = filed

    def __call__(self, value):
        result = value.get(self.filed)
        if result and not result.startswith('https://www.youtube.com/'):
            raise ValidationError('is not okay')
