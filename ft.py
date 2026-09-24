import math
def fourier_transform(wave, sample_rate):
    frequency_range = sample_rate//2 #check every 10 to speed it up
    is_present=dict()
    num_samples = len(wave)
    for f in range(0, frequency_range, 10):
        sum_sin = 0
        sum_cos = 0
        for idx, i in enumerate(wave):
            t=idx/sample_rate
            artificial_sample_part_sin = math.sin(2*math.pi*f*t)
            artificial_sample_part_cos = math.cos(2 * math.pi * f * t)
            sum_sin+=artificial_sample_part_sin*i
            sum_cos+=artificial_sample_part_cos*i
        vector_length = math.sqrt(sum_sin**2+sum_cos**2)
        vector_length_normalized = vector_length/num_samples
        is_present[f]=(True if vector_length_normalized>0.05 else False, sum_sin, sum_cos)
    return is_present


