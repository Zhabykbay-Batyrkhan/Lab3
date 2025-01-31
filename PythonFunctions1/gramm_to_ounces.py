def ounce(gramm):
    return gramm / 28.3495231

gramm = int(input())
ounces = ounce(gramm)
print(f"{gramm} grams is equal to {ounces:.2f} ounces")
