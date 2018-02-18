text = "X-DSPAM-Confidence:    0.8475";
pos= text.find('.');
float_string= text[pos-1:];
print float(float_string);