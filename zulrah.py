import random
import matplotlib.pyplot as plot
import numpy as np

total_count = 0
counts = []
sample_size = 10000

for _ in range (sample_size): 
    counter = 0
    drops = [0 , 0 , 0, 0]
    if _ % 1000 == 0:
        print(f'{_} Iterations completed')
    while min(drops) < 5:
        if random.randint(1, 512) == 1:
            drops[0] += 1

        if random.randint(1,512) == 1:
            drops[1] += 1
        
        if random.randint(1, 512) == 1:
            drops[2] += 1
        
        if random.randint(1, 512) == 1:
            drops[3] += 1

        counter += 1
    
    total_count += counter
    counts.append(counter)

print(counts)
average_count = total_count/ sample_size

plot.figure(figsize=(10,6))
plot.hist(counts, bins=30, edgecolor='black')
plot.xlabel('KC for uniques')
plot.ylabel('Frequency')
plot.title(f'Zulrah Uniques KC: {sample_size} simulations')
plot.figtext(.60, .72, f'Fastest unique completion: {min(counts)}')
plot.figtext(.60, .75, f'Slowest unique completion: {max(counts)}')
plot.figtext(.60, .80, f'Average unique completion: {average_count}')
plot.figtext(.60, .83, f'Median unique completion: {np.median(counts)}')
            
plot.show()