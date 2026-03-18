def hello_name(name):
    return "Hello " + name + "!"

def make_abba(a, b):
    return a + b + b + a

def make_tags(tag, word):
    return "<{}>{}</{}>".format(tag, word, tag)

def make_out_word(out, word):
    return out[:2] + word + out[2:]

def extra_end(s):
    return s[-2:] * 3

def first_two(s):
    return s[:2]

def first_half(s):
    return s[:len(s)//2]

def without_end(s):
    return s[1:-1]

def combo_string(a, b):
    return a + b + a if len(a) < len(b) else b + a + b

def non_start(a, b):
    return a[1:] + b[1:]

def left2(s):
    return s[2:] + s[:2]