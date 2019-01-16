text = "X-DSPAM-Confidence:    0.8475";
valpos = text.find('0')
value = float(text[valpos:])
print(value)
