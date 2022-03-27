"""Question 1"""

def u(z, theta) -> float:
    
    """ Defining utility function. 

    Args:
        z(float): parameter 
        theta(float): parameter

    Returns:
        Utility of assets

    """ 
    return (z**(1 + theta)) / (1 + theta)


def pi(p, q):
    
    """ Defining premium policy function. 

    Args:
        p(float): probability of monetary loss
        q(float): coverage amount

    Returns:
        Premium policy 

    """ 
    return (p * q)


def V(q, x, y, p) -> float:
    first_term = p * u(y - x + q - pi(p, q), theta)

    second_term = (1-p) * u(y - pi(p, q), theta)
    
    """ Defining function for the expected utility if insured.

    Args:
        p(float): probability of monetary loss
        q(float): coverage amount
        x(float): monetary loss
        y(float): assets 

    Returns:
        Expected utility for insured agent.

    """
    return first_term + second_term


def q_star(x, y, p):
    obj = lambda q: -V(q, x, y, p)
    res = optimize.minimize_scalar(obj, bounds = (0, x), method = 'bounded')
    
    """ Calculating the optimal insurance coverage q for the insured agent, 
    using the expected utility function.

    Args:
        p(float): probability of monetary loss
        q(float): coverage amount
        x(float): monetary loss
        y(float): assets 

    Returns:
        Optimal insurance coverage.

    """  
    return res.x


"""Question 2"""

def V_null(p:float) -> float:
     
    """ Defining function for the expected utility if not insured.

    Args:
        p(float): probability of monetary loss
        x(float): monetary loss
        y(float): assets 

    Returns:
        Expected utility for agent who is not insured.

    """
    return p*u(y - x, theta) + (1 - p)*u(y, theta)



def V_pi(pi, q, x, y, p) -> float:
    first_term = p * u(y - x + q - pi, theta)

    second_term = (1-p) * u(y - pi, theta)
    
    """ Defining function for the expected utility if insured, 
    where premium policy pi is no longer a function.

    Args:
        pi(float): insurance premium
        q(float): coverage amount
        p(float): probability of monetary loss
        x(float): monetary loss
        y(float): assets 

    Returns:
        Expected utility for insured agent.

    """
    return first_term + second_term 


def pi_star(q, x, y, p, V_null): 
    def obj(pi):
        return V_pi(pi, q, x, y, p) - V_null
    obj = lambda pi: V_pi(pi, q, x, y, p) - V_null
    res = optimize.root_scalar(obj, bracket=[0, q], method='brentq')

    """ Calculating the optimal insurance premium pi for the insured agent, 
    using the expected utility function of being and not being insured.

    Args:
        p(float): probability of monetary loss
        q(float): coverage amount
        x(float): monetary loss
        y(float): assets 
        V_null(func): function for expected utility if not insured

    Returns:
        Optimal insurance premium such that expected utility of having an insurance
        is at least as good as expected utility of not having an insurance. 

    """  
    return res.root


"""Question 3"""

def V_beta(gamma, pi):
    
    """ Defining function for the expected utility for insured agent, 
    where we know the coverage ratio gamma and x is drawn from beta
    distribution.

    Args:
        pi(float): insurance premium
        gamma(float): coverage ratio

    Returns:
        Expected utility for agent.

    """   
    return u(y-(1-gamma)*x-pi, theta)


def monte_carlo(y, p, N, gamma, pi):
    x = np.random.beta(alpha, beta, N)
    
    """ Calculating expected utility for insured agent by 
    Monte Carlo integration.

    Args:
        pi(float): insurance premium
        gamma(float): coverage ratio
        y(float): assets 
        p(float): probability of monetary loss
        
    Returns:
        Expected utility for insured agent using
        at least 10 000 draws.

    """     
    return np.mean(V_beta(x, pi))


"""Question 4"""


def monte_carlo2(p, gamma1, x): 
    def obj(pi): 
        return -p * (gamma1 * x)
    obj = lambda pi: -p * (gamma1 * x)
    res = optimize.root(obj, bracket=[0, q], method='broyden1')
  
    """ Calculating profit maximizing premium by Monte carlo integration
    given that a customer wants a coverage ratio gamma of 0.95.

    Args:
        gamma1(float): coverage ratio
        p(float): probability of monetary loss
        x(float): monetary loss
    Returns:
        Optimal insurance premium from insurance company's point of view.

    """ 
    return res.root