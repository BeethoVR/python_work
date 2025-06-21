import time

Seg     = input('Cuantos segundos:')
nSeg    = int(Seg)
while nSeg > 0:
    time.sleep(1)
    print(f"00:{nSeg:02d}")
    nSeg -= 1
