text = "X-DSPAM-Confidence:    0.8475"
start = text.find(':')
nss = text[start + 1:]
nws = nss.strip()
nf = float(nws)
print(nf)