def emulate(pattern: str):
    while "01" in pattern or "02" in pattern or "03" in pattern:
        pattern = pattern.replace("01", "30", 1)
        pattern = pattern.replace("02", "311230", 1)
        pattern = pattern.replace("03", "1230", 1)
    return pattern

print(emulate("01233"))
