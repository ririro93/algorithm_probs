## 멀쩡한_사각형
import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w, h))