import numpy as np

def generate_spectra(B_neg, B_pos, mu_neg, mu_pos, n_neg, n_pos, beta_std_neg='auto', beta_std_pos='auto', epsilon_std=0, random_state=42):
    """
    | Parameters |
    --------------
    B_neg : 2-D Array
        Matrix containing the calibration vectors which model the intrinsic biological variability for the negative (control) class.
        Observations are in the rows and the wavenumbers are in the columns.
    B_pos : 2-D Array
        Same as B_neg, but for the positive (case) class.
    mu_neg : 1-D Array
        Mean spectrum across the wavenumbers for the negative class.
    mu_pos : 1-D Array
        Mean spectrum across the wavenumbers for the positive class.
    n_pos : Int
        Number of positive class samples to be generated.
    n_neg : Int
        Number of negative class samples to be generated.
    beta_std_neg : Float
        Standard deviation around the biological variability of the negative class samples. 
        The higher, the more variance with zero being no variance.
        Defaults to 1/sqrt(X_neg.shape[0]), i.e., using the number of negative class samples used for calibration.
    beta_std_pos : Float
        Same as beta_std_neg but for the postive class.
    epsilon_std : 1-D Array
        Standard deviation around the additative white noise across the spectrum. 
        The higher, the more variance with zero being no variance.
    random_state : Int or None
        Controls the pseudo-random number generator's random seed. 
        Pass an int for reproducible results across multiple runs with the same parameters.
    | Returns |
    -----------
    X_gen : 2-D Matrix
        Generated spectra with n_neg+n_pos observations.
    y_gen : 1-D Vector
        Labels of generated spectra.
    """    
    # set random state for the numpy random number generator
    rand = np.random.RandomState(random_state)

    # number of calibration vectors modeling variability
    m_neg = B_neg.shape[0]
    m_pos = B_pos.shape[0]
    
    # to model the biological variability, if 'auto', set to the calibrated level based on the given vectors
    if beta_std_neg == 'auto':
        beta_std_neg = 1/np.sqrt(m_neg)
    if beta_std_pos == 'auto':
        beta_std_pos = 1/np.sqrt(m_pos)

    BETA_neg = rand.normal(0, beta_std_neg, (m_neg, n_neg)).T
    BETA_pos = rand.normal(0, beta_std_pos, (m_pos, n_pos)).T
    
    # generated class samples with modeled variability
    X_neg_gen = np.tile(mu_neg, (n_neg, 1)) + BETA_neg @ B_neg
    X_pos_gen = np.tile(mu_pos, (n_pos, 1)) + BETA_pos @ B_pos
    
    # put simulated samples in one matrix
    X_gen = np.vstack([X_neg_gen, X_pos_gen])

    # add measurement white noise
    X_gen += rand.normal(0, epsilon_std, X_gen.shape)
    
    # create class labels for simulated samples
    y_gen = np.hstack([np.zeros(n_neg), np.ones(n_pos)])
    
    return X_gen, y_gen