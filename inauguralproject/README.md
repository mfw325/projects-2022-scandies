# Inaugural project

The **results** of the project can be seen from running [inauguralproject.ipynb](inauguralproject.ipynb).

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires no further packages.

In this project we will analyze and calculate outcomes using Mossin's model, a model for insurance policies. Within the model there is an agent that has assets y from which they get utility u('), but they could also suffer a monetary loss x with a probability p. The insurance company has a premium policy function depending on coverage amount q and probability of loss being incurred p. In order to mitigate the loss, the agent could choose to purchase an insurance. The insurance contract contains a coverage amount q (which will be payed out if the agent would suffer a monetary loss) and a premium pi (to be paid by the agent in any case). The coverage amount cannot be higher than the monetary loss and the insurance company must require a higher premium in order to be able to provide better coverage. 

In this assignment we will analyze the optimal insurance premiums and coverage amounts from both the agent's and insurance company's poitn of view, as well as evaluating different policies. 

In the first question, we are asked to calculate the optimal coverage amount for the agent, for each possible monetary loss in the range 0,01-0,9. When plotting the graph, we get a completely linear graph and it is clear that a higher monetary loss q will also entail a higher optimal coverage amount q. This would make sense as the agent expects to be compensated a higher amount, the higher the monetary loss is.

In the second question we are asked to find the set of acceptable contracts from the agent's point of view, which would be contracts that ensure an expected value at least as good as if not having an insurance. When we plot the insurance company's premium policy function as well as the function for the acceptable premiums given the range of q. The red graph shows for each coverage amount, the acceptable premium level from the agent's point of view. The blue graph shows for each coverage amount, the premium level that is needed for the insurance to at least break even at each q. The area between these graphs capture the set of feasible premiums for a given q.

In the third question we modify the model through thinking of x as drawn from a beta distribution and that the agent's value is written as the integral of the expression from before. The monte carlo fucntion is now used to compute the optimization, using 10 000 draws. We are asked to test out two sets of insurance policies with different values for coverage ratio gamma and premium pi. We conclude that the policy with the lower insurance premium (0,1) and coverage ratio (0,45) is preferable to the agent. Both policies yield negative utility, but the point is that the agent does not get utility from insurance but from assets. The insurance policy is there to mitigate the loss in case something happens, and will not yield utility itself, so the policy that provides the smallest loss is preferable.  

In the fourth question we instead look at the profit maximizing premium from the insurance company's point of view.  
We were not able to solve for the profit maximizing premium, but will correct this at a later point. 


