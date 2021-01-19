# Modul for functions
import scipy.stats, math

def sample_dist_mean(data_input,sample_size, sample_bucket):
    '''
    Function to calculate the sample distribution of the mean.
    
    Input:  dat_input = Data to be sampled from.
            sample_size = numer of samples where each sample is drawing 10 values and calculating mean
    
    Output: printing calculation time
            samples = array of the sample means
    '''
    start = time.time()
    samples = np.zeros(sample_size)
    for s in range(sample_size):                 
        samples[s] = data_input.sample(n=sample_bucket, replace ='true').mean()
    print(time.time()- start)
    return samples

def p_value_t_stat(Null_hypothesis_value,sample_mean,sample_sd,sample_size):
    '''
    Function to calculate the p-value. It takes the degrees of freedom to get the correspondig t-distribution
    and calculates the t-value to get the p-value
    
    Input:  test_value = The value to be tested acording to the hypothesis
            sample_mean = mean of the sample
            samle_sd = standard deviation of the sample
            sample_size = size of the sample
            
    Output: pval = P value
    '''
    t_dist = scipy.stats.t(sample_size-1)
    t = (sample_mean - Null_hypothesis_value)/(sample_sd/math.sqrt(sample_size))
    pval = 1 - t_dist.cdf(t)
    return pval