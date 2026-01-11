#1
def rectangle_info(width, height):
    S = width * height
    P = 2 * (width + height)
    return (S, P)

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

def safe_div(a, b):
    if b == 0:
        return None
    else: return a/b

#2
def delivery_price(city, weight_kg, urgent):
    if urgent == True:
        price = 500 + 30 * weight_kg
    else: price =300 + 20 * weight_kg
    return price
print(delivery_price('Самара', 50, True))
print(delivery_price('Москва', 40, False))
print(delivery_price(city='Москва', weight_kg=40, urgent=False))
print(delivery_price(city='Самара', weight_kg=50, urgent=True))
#print(delivery_price(city='Пермь', weight_kg=33, False))

#3
def push_score(score, scores=None):
    scores = []
    scores.append(score)
    return scores

print(push_score(3))
print(push_score(34))
spisok = []
print(push_score(2, spisok))

def top_scores(scores, n=3):
    return n

#4
def make_multiplier(factor):
    def mul(x):
        return x * factor

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))
print(triple(10))


def mean(*args):
    if not args:
        return None
    return sum(args)/len(args)

def build_profile(**kwargs):
    name=kwargs.get("name", "Без имени")
    age=kwargs.get("age", 0)
    return kwargs





