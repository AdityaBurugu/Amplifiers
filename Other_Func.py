def format_value(value):
    if abs(value) >= 1e6:
        formatted_value = round(value / 1e6,2)
        unit = 'M'
    elif abs(value) >= 1e3:
        formatted_value = round(value / 1e3,2)
        unit = 'k'
    else:
        formatted_value = round(value,2)
        unit = ''

    return f"{formatted_value}{unit}"