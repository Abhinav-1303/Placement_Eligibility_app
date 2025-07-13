month_conversion = {
    "jan": "january",
    "feb": "february",
    "mar": "march"
}

print(month_conversion["jan"])
print(month_conversion.get("feb"))
print(month_conversion.get("dec"))
print(month_conversion.get("dec", "not valid"))