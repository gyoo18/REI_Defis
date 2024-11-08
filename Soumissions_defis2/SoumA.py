import time

def main():
    timer = time.time()
    valeur = 2

    while time.time()-timer <= 9:
        valeur = valeur*2
    
    return valeur