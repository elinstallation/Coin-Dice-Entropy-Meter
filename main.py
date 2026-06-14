import math

# H = -sum(p*log2(p)) for each outcome p

def is_safe(p):
    if p <= 0.0:
        return 0.0
    return p*math.log2(p)


def entropy(probabilities):
    #probabilities -> list of floats that should sum to 1

    #returns H, entropy in bits
    total = 0.0
    for p in probabilities:
        total = total + is_safe(p)
    return -total

def max_entropy(num_outcomes):
    #highest possible entropy for a given number of outcomes
    #happens when all outcomes are equally likely

    return math.log2(num_outcomes)

def normalise(weights):
    total = sum(weights)
    result = []
    for w in weights:
        result.append(w/total)
    return result

def coin_entropy(p):
    return entropy([p, 1.0 - p])

def coin_curve(num_points=300):

    p_values = []
    h_values = []
 
    for i in range(num_points):
        p = i / (num_points - 1)   # evenly spaced from 0.0 to 1.0
        h = coin_entropy(p)
        p_values.append(p)
        h_values.append(h)
 
    return p_values, h_values

def die_entropy(weights):
    probs = normalise(weights)
    return entropy(probs)

def entorpy_ratio(h, num_outcomes):
    h_max = max_entropy(num_outcomes)
    return h/h_max