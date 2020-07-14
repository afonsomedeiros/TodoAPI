necessário fazer uma leve alteração no arquivo `fields.py` do marshmallow (tomei liberdade de fazer essa modificação por ser mais simples que criar um custom field).

A partir da linha 1191.
```py
def _serialize(self, value, attr, obj, **kwargs):
    if value is None:
        return None
    data_format = self.format or self.DEFAULT_FORMAT
    format_func = self.SERIALIZATION_FUNCS.get(data_format)
    if format_func:
        return format_func(value)
    else:
        if isinstance(value, str):
            return value
        return value.strftime(data_format)
```