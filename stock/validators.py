from django.core.exceptions import ValidationError 

def validate_symbol(value):
    if value.lengt()  != 4:
        msg = u"4자리 심볼코드를 입력해주세요."
        raise ValidationError(msg)