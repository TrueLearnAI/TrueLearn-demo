from collections import deque
from truelearn.models import Knowledge, HistoryAwareKnowledgeComponent


knowledge_dict = {
    15809: {
        'mean': 0.7447557848684493,
        'variance': 0.3402576248032043,
        'timestamp': 2597189.0,
        'title': 'Machine learning',
        'description': 'Study of algorithms that improve automatically through experience',
        'url': 'https://en.wikipedia.org/wiki/Machine_learning',
        'history': deque([(0.0, 0.5, 6095.0), (0.40088867391203176, 0.4242286769661634, 6095.0), (0.563420660725972, 0.37905195116627616, 9129.0)])
    },
    4875: {
        'mean': 0.40088867391203176,
        'variance': 0.4242286769661634,
        'timestamp': 6095.0,
        'title': 'Cognitive science',
        'description': 'Interdisciplinary scientific study of the mind, the gut and its processes',
        'url': 'https://en.wikipedia.org/wiki/Cognitive_science',
        'history': deque([(0.0, 0.5, 6095.0)])
    },
    692: {
        'mean': 0.6604218273313369,
        'variance': 0.3713110359437446,
        'timestamp': 2500723.0,
        'title': 'Algorithm',
        'description': 'Sequence of operations for a task',
        'url': 'https://en.wikipedia.org/wiki/Algorithm',
        'history': deque([(0.0, 0.5, 6095.0), (0.40088867391203176, 0.4242286769661634, 6095.0)])
    },
    13443: {
        'mean': 0.40088867391203176, 
        'variance': 0.4242286769661634,
        'timestamp': 6095.0,
        'title': 'Information retrieval',
        'description': 'Obtaining information resources relevant to an information need',
        'url': 'https://en.wikipedia.org/wiki/Information_retrieval',
        'history': deque([(0.0, 0.5, 6095.0)])
    },
    9684: {
        'mean': 0.40088867391203176,
        'variance': 0.4242286769661634,
        'timestamp': 6095.0,
        'title': 'Feast of Corpus Christi',
        'description': 'Catholic feast day, public holiday in some countries',
        'url': 'https://en.wikipedia.org/wiki/Feast_of_Corpus_Christi',
        'history': deque([(0.0, 0.5, 6095.0)])
    },
    25935: {
        'mean': 0.35672268806506674,
        'variance': 0.42713970733735107,
        'timestamp': 9129.0,
        'title': 'Star (graph theory)',
        'description': 'Tree graph with one central node and leaves of length 1',
        'url': 'https://en.wikipedia.org/wiki/Star_(graph_theory)',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    29069: {
        'mean': 0.35672268806506674,
        'variance': 0.42713970733735107,
        'timestamp': 9129.0,
        'title': 'Variational message passing',
        'description': '',
        'url': 'https://en.wikipedia.org/wiki/Variational_message_passing',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    16688: {
        'mean': 0.35672268806506674,
        'variance': 0.42713970733735107,
        'timestamp': 9129.0,
        'title': 'Message passing',
        'description': 'Technique for running a program on a computer without directly calling it',
        'url': 'https://en.wikipedia.org/wiki/Message_passing',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    11574: {
        'mean': 0.35672268806506674,
        'variance': 0.42713970733735107,
        'timestamp': 9129.0,
        'title': 'Graph (discrete mathematics)',
        'description': 'Vertices connected in pairs by edges',
        'url': 'https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    13454: {
        'mean': 0.35672268806506674,
        'variance': 0.42713970733735107,
        'timestamp': 9129.0,
        'title': 'Information theory',
        'description': 'Scientific study of digital information',
        'url': 'https://en.wikipedia.org/wiki/Information_theory',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    2279: {
        'mean': 0.5577640588475082,
        'variance': 0.3793320712505449,
        'timestamp': 9129.0,
        'title': 'Belief propagation',
        'description': 'Algorithm for statistical inference on graphical models',
        'url': 'https://en.wikipedia.org/wiki/Belief_propagation',
        'history': deque([(0.0, 0.5, 9129.0), (0.3950956928111329, 0.4245846436791379, 9129.0)])
    },
    20941: {
        'mean': 1.0903355942521082,
        'variance': 0.2688628497420236,
        'timestamp': 2500723.0,
        'title': 'Posterior probability',
        'description': 'Conditional probability used in Bayesian statistics',
        'url': 'https://en.wikipedia.org/wiki/Posterior_probability',
        'history': deque([(0.0, 0.5, 9129.0), (0.3950956928111329, 0.4245846436791379, 9129.0), (0.5816289693479033, 0.3781785004556414, 9129.0), (0.8260225257574929, 0.33629427290466307, 9129.0), (0.8434980551930927, 0.3276694487609885, 2167926.0), (0.9855604320776528, 0.2993878857149642, 2167926.0), (1.0353980341412936, 0.2839918215494356, 2500723.0)])
    },
    29054: {
        'mean': 0.39509569281113277,
        'variance': 0.4245846436791379,
        'timestamp': 9129.0,
        'title': 'Variance',
        'description': 'Statistical measure of how far values spread from their average',
        'url': 'https://en.wikipedia.org/wiki/Variance',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    9326: {
        'mean': 0.8915775888886187,
        'variance': 0.3047980737119745,
        'timestamp': 2167926.0,
        'title': 'Expectation propagation',
        'description': 'Method to approximate a probability distribution',
        'url': 'https://en.wikipedia.org/wiki/Expectation_propagation',
        'history': deque([(0.0, 0.5, 9129.0), (0.39509569281113277, 0.4245846436791379, 9129.0), (0.5816289693479032, 0.3781785004556414, 9129.0), (0.7265180501355146, 0.3422773490041454, 9129.0), (0.8753524105698773, 0.31223286055838756, 2167926.0)])
    },
    2200: {
        'mean': 0.6186055843254298,
        'variance': 0.37551717934123163,
        'timestamp': 2500723.0,
        'title': 'Bayesian inference',
        'description': 'Method of statistical inference',
        'url': 'https://en.wikipedia.org/wiki/Bayesian_inference',
        'history': deque([(0.0, 0.5, 9129.0), (0.39509569281113277, 0.4245846436791379, 9129.0)])
    },
    18462: {
        'mean': 0.7721548092601376,
        'variance': 0.32341512064215905,
        'timestamp': 2500723.0,
        'title': 'Normalizing constant',
        'description': 'Constant a such that af(x) is a probability measure',
        'url': 'https://en.wikipedia.org/wiki/Normalizing_constant',
        'history': deque([(0.0, 0.5, 9129.0), (0.3762289469953915, 0.4257963899933523, 9129.0), (0.6003767261282469, 0.37644845313124364, 2500723.0), (0.7149396636766843, 0.3437067747607554, 2500723.0)])
    },
    6221: {
        'mean': 0.3762289469953915,
        'variance': 0.4257963899933523,
        'timestamp': 9129.0,
        'title': 'Covariance matrix',
        'description': 'Measure of covariance of components of a random vector',
        'url': 'https://en.wikipedia.org/wiki/Covariance_matrix',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    25899: {
        'mean': 0.4585982724308978,
        'variance': 0.39178677644715315,
        'timestamp': 2500723.0,
        'title': 'Standard deviation',
        'description': 'In statistics, a measure of variation',
        'url': 'https://en.wikipedia.org/wiki/Standard_deviation',
        'history': deque([(0.0, 0.5, 9129.0), (0.3762289469953915, 0.4257963899933523, 9129.0)])
    },
    13260: {
        'mean': 0.5632945814817174,
        'variance': 0.3791249865143275,
        'timestamp': 9129.0,
        'title': 'Indicator function',
        'description': 'Mathematical function characterizing set membership',
        'url': 'https://en.wikipedia.org/wiki/Indicator_function',
        'history': deque([(0.0, 0.5, 9129.0), (0.3762289469953915, 0.4257963899933523, 9129.0)])
    },
    13505: {
        'mean': 0.3762289469953915,
        'variance': 0.4257963899933523,
        'timestamp': 9129.0,
        'title': 'Inner product space',
        'description': 'Generalization of the dot product; used to define Hilbert spaces',
        'url': 'https://en.wikipedia.org/wiki/Inner_product_space',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    9526: {
        'mean': 0.21966559473325556,
        'variance': 0.43564431466985426,
        'timestamp': 9129.0,
        'title': 'Factor graph',
        'description': '',
        'url': 'https://en.wikipedia.org/wiki/Factor_graph',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    18442: {
        'mean': 0.21966559473325561,
        'variance': 0.43564431466985426,
        'timestamp': 9129.0,
        'title': 'Normal distribution',
        'description': 'Probability distribution',
        'url': 'https://en.wikipedia.org/wiki/Normal_distribution',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    12894: {
        'mean': 0.48663089769352447,
        'variance': 0.38106260707103834,
        'timestamp': 9129.0,
        'title': 'Hyperplane',
        'description': 'Subspace of n-space whose dimension is (n-1)',
        'url': 'https://en.wikipedia.org/wiki/Hyperplane',
        'history': deque([(0.0, 0.5, 9129.0), (0.3231193155019874, 0.4267855425970243, 9129.0)])
    },
    15212: {
        'mean': 0.3231193155019874,
        'variance': 0.4267855425970243,
        'timestamp': 9129.0,
        'title': 'Linear classifier',
        'description': 'Statistical classification in machine learning',
        'url': 'https://en.wikipedia.org/wiki/Linear_classifier',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    9689: {
        'mean': 0.3231193155019874,
        'variance': 0.4267855425970243,
        'timestamp': 9129.0,
        'title': 'Feature (machine learning)',
        'description': '',
        'url': 'https://en.wikipedia.org/wiki/Feature_(machine_learning)',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    28085: {
        'mean': 0.3231193155019874,
        'variance': 0.4267855425970243,
        'timestamp': 9129.0,
        'title': 'Training, validation, and test data sets',
        'description': 'Tasks in machine learning',
        'url': 'https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    25489: {
        'mean': 0.19156176331156388,
        'variance': 0.43724407784615,
        'timestamp': 9129.0,
        'title': 'Spamming',
        'description': 'Unsolicited electronic messages, especially advertisements',
        'url': 'https://en.wikipedia.org/wiki/Spamming',
        'history': deque([(0.0, 0.5, 9129.0)])
    },
    27892: {
        'mean': 0.7095388575489646,
        'variance': 0.33388560329002226,
        'timestamp': 2597189.0,
        'title': 'Topic model',
        'description': 'Statistical model',
        'url': 'https://en.wikipedia.org/wiki/Topic_model',
        'history': deque([(0.0, 0.5, 2167926.0), (0.32539770281959385, 0.4295127560649423, 2167926.0), (0.5121651197501016, 0.38220191949952786, 2167926.0), (0.5320262397057491, 0.3710616157145398, 2167926.0)])
    },
    1273: {
        'mean': 0.6211904677541206,
        'variance': 0.3634476984284803,
        'timestamp': 2167926.0,
        'title': 'Approximate inference',
        'description': '',
        'url': 'https://en.wikipedia.org/wiki/Approximate_inference',
        'history': deque([(0.0, 0.5, 2167926.0), (0.32539770281959385, 0.4295127560649423, 2167926.0), (0.6017492230150165, 0.37412195653311, 2167926.0)])
    },
    24344: {
        'mean': 0.32539770281959385,
        'variance': 0.4295127560649423,
        'timestamp': 2167926.0,
        'title': 'Sesame Street',
        'description': "American children's television show",
        'url': 'https://en.wikipedia.org/wiki/Sesame_Street',
        'history': deque([(0.0, 0.5, 2167926.0)])
    },
    3978: {
        'mean': 0.32539770281959385,
        'variance': 0.4295127560649423,
        'timestamp': 2167926.0,
        'title': 'Central processing unit',
        'description': 'Central computer component which executes instructions',
        'url': 'https://en.wikipedia.org/wiki/Central_processing_unit',
        'history': deque([(0.0, 0.5, 2167926.0)])
    },
    15160: {
        'mean': 0.32539770281959385,
        'variance': 0.4295127560649423,
        'timestamp': 2167926.0,
        'title': 'Likelihood function',
        'description': 'Function related to statistics and probability theory',
        'url': 'https://en.wikipedia.org/wiki/Likelihood_function',
        'history': deque([(0.0, 0.5, 2167926.0)])
    },
    5609: {
        'mean': 0.2174177766472068,
        'variance': 0.4358866450746774,
        'timestamp': 2167926.0,
        'title': 'Conjugate prior',
        'description': 'Concept in probability theory',
        'url': 'https://en.wikipedia.org/wiki/Conjugate_prior',
        'history': deque([(0.0, 0.5, 2167926.0)])
    },
    9380: {
        'mean': 0.7015469276137397,
        'variance': 0.33705961799330453,
        'timestamp': 2167926.0,
        'title': 'Exponential family',
        'description': 'Family of probability distributions related to the normal distribution',
        'url': 'https://en.wikipedia.org/wiki/Exponential_family',
        'history': deque([(0.0, 0.5, 2167926.0), (0.2174177766472068, 0.4358866450746774, 2167926.0), (0.4978703017430074, 0.3788396691567734, 2167926.0)])
    },
    3441: {
        'mean': 0.8887825056319612,
        'variance': 0.30448112740364863,
        'timestamp': 2167926.0,
        'title': 'Calculus of variations',
        'description': 'Differential calculus on function spaces',
        'url': 'https://en.wikipedia.org/wiki/Calculus_of_variations',
        'history': deque([(0.0, 0.5, 2167926.0), (0.2174177766472068, 0.4358866450746774, 2167926.0), (0.4978703017430074, 0.3788396691567734, 2167926.0), (0.7015469276137397, 0.33705961799330453, 2167926.0)])
    },
    5519: {
        'mean': 0.7263720241643755,
        'variance': 0.32731682957159497,
        'timestamp': 2167926.0,
        'title': 'Conditional probability distribution',
        'description': '',
        'url': 'https://en.wikipedia.org/wiki/Conditional_probability_distribution',
        'history': deque([(0.0, 0.5, 2167926.0), (0.321703507396691, 0.4249370704939545, 2167926.0), (0.5501636074655295, 0.37237078260102463, 2167926.0), (0.5695138524640412, 0.36179621784359434, 2167926.0)])
    },
    16388: {
        'mean': 0.32170350739669096,
        'variance': 0.4249370704939545,
        'timestamp': 2167926.0,
        'title': 'Maximum likelihood estimation',
        'description': 'Method of estimating the parameters of a statistical model, given observations',
        'url': 'https://en.wikipedia.org/wiki/Maximum_likelihood_estimation',
        'history': deque([(0.0, 0.5, 2167926.0)])
    }, 
    14765: {
        'mean': 0.5061370845893377,
        'variance': 0.37488334129211087,
        'timestamp': 2167926.0,
        'title': 'Latent and observable variables',
        'description': 'Variable not directly observed',
        'url': 'https://en.wikipedia.org/wiki/Latent_variable',
        'history': deque([(0.0, 0.5, 2167926.0), (0.26881639180511185, 0.4272223414930943, 2167926.0)])
    },
    5951: {
        'mean': 0.26881639180511185,
        'variance': 0.4272223414930943,
        'timestamp': 2167926.0,
        'title': 'Coordinate descent',
        'description': '',
        'url': 'https://en.wikipedia.org/wiki/Coordinate_descent',
        'history': deque([(0.0, 0.5, 2167926.0)])
    },
    15552: {
        'mean': 0.5012633585135846,
        'variance': 0.37637682588147475,
        'timestamp': 2167926.0,
        'title': 'Log probability',
        'description': 'Logarithm of probabilities, useful for calculations',
        'url': 'https://en.wikipedia.org/wiki/Log_probability',
        'history': deque([(0.0, 0.5, 2167926.0), (0.2777484575769335, 0.42831017518644765, 2167926.0)])
    },
    29070: {
        'mean': 0.27774845757693345,
        'variance': 0.42831017518644765,
        'timestamp': 2167926.0,
        'title': 'Variational method (quantum mechanics)',
        'description': '',
        'url': 'https://en.wikipedia.org/wiki/Variational_method_(quantum_mechanics)',
        'history': deque([(0.0, 0.5, 2167926.0)])
    },
    21367: {
        'mean': 0.8129212685744592,
        'variance': 0.29816459890019503,
        'timestamp': 2500723.0,
        'title': 'Probability',
        'description': 'Branch of mathematics concerning chance and uncertainty',
        'url': 'https://en.wikipedia.org/wiki/Probability',
        'history': deque([(0.0, 0.5, 2167926.0), (0.27774845757693345, 0.42831017518644765, 2167926.0), (0.5012633585135846, 0.37637682588147475, 2167926.0), (0.695585946624534, 0.3364620586514054, 2500723.0), (0.7515951005972729, 0.3170168117651694, 2500723.0)])
    },
    23575: {
        'mean': 0.4433381496269409,
        'variance': 0.3807890189385727,
        'timestamp': 2167926.0,
        'title': 'Sampler (musical instrument)',
        'description': 'Device that records and plays back samples',
        'url': 'https://en.wikipedia.org/wiki/Sampler_(musical_instrument)',
        'history': deque([(0.0, 0.5, 2167926.0), (0.21677696444044198, 0.4341476139220864, 2167926.0)])
    },
    16167: {
        'mean': 0.6762959392307157,
        'variance': 0.3381537249052618,
        'timestamp': 2500723.0,
        'title': 'Markov chain',
        'description': 'Random process independent of past history',
        'url': 'https://en.wikipedia.org/wiki/Markov_chain',
        'history': deque([(0.0, 0.5, 2167926.0), (0.21677696444044198, 0.4341476139220864, 2167926.0), (0.4433381496269409, 0.3807890189385727, 2167926.0)])
    },
    12311: {
        'mean': 0.21677696444044192,
        'variance': 0.4341476139220864,
        'timestamp': 2167926.0,
        'title': 'Hidden-variable theory',
        'description': 'Theory regarding quantum mechanics',
        'url': 'https://en.wikipedia.org/wiki/Hidden-variable_theory',
        'history': deque([(0.0, 0.5, 2167926.0)])
    },
    10857: {
        'mean': 0.26092644289778183,
        'variance': 0.4292266819350053,
        'timestamp': 2167926.0,
        'title': 'Gamma function',
        'description': 'Extension of the factorial function',
        'url': 'https://en.wikipedia.org/wiki/Gamma_function',
        'history': deque([(0.0, 0.5, 2167926.0)])
    },
    22737: {
        'mean': 0.6246270146829009,
        'variance': 0.3698506437110491,
        'timestamp': 2500723.0,
        'title': 'Rejection sampling',
        'description': 'Computational statistics technique',
        'url': 'https://en.wikipedia.org/wiki/Rejection_sampling',
        'history': deque([(0.0, 0.5, 2500723.0), (0.30588827148053166, 0.4264910127555862, 2500723.0)])
    },
    13142: {
        'mean': 0.7371820692867409,
        'variance': 0.3382465994026892,
        'timestamp': 2500723.0,
        'title': 'Importance sampling',
        'description': 'Distribution estimation technique',
        'url': 'https://en.wikipedia.org/wiki/Importance_sampling',
        'history': deque([(0.0, 0.5, 2500723.0), (0.30588827148053166, 0.4264910127555862, 2500723.0), (0.6246270146829009, 0.3698506437110491, 2500723.0)])
    },
    9333: {
        'mean': 0.6402797008061846,
        'variance': 0.34270769116414396,
        'timestamp': 2500723.0,
        'title': 'Expected value',
        'description': 'Average value of a random variable',
        'url': 'https://en.wikipedia.org/wiki/Expected_value',
        'history': deque([(0.0, 0.5, 2500723.0), (0.3058882714805317, 0.4264910127555862, 2500723.0), (0.5260847121371206, 0.3752393903275519, 2500723.0)])
    },
    28714: {
        'mean': 0.5021475665420293,
        'variance': 0.3809777340922654,
        'timestamp': 2500723.0,
        'title': 'Continuous uniform distribution',
        'description': 'Uniform distribution on an interval',
        'url': 'https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)',
        'history': deque([(0.0, 0.5, 2500723.0), (0.37367580285335633, 0.4221522051247657, 2500723.0)])
    },
    21373: {
        'mean': 0.7209006535539564,
        'variance': 0.32543582461667464,
        'timestamp': 2500723.0,
        'title': 'Probability distribution',
        'description': 'Mathematical function for the probability a given outcome occurs in an experiment',
        'url': 'https://en.wikipedia.org/wiki/Probability_distribution',
        'history': deque([(0.0, 0.5, 2500723.0), (0.37367580285335633, 0.4221522051247657, 2500723.0), (0.5916321259730537, 0.37193807143277885, 2500723.0), (0.6535467941371249, 0.3481760963826483, 2500723.0)])
    },
    16320: {
        'mean': 0.37367580285335633,
        'variance': 0.4221522051247657,
        'timestamp': 2500723.0,
        'title': 'Mathematical proof',
        'description': 'Reasoning for mathematical statements',
        'url': 'https://en.wikipedia.org/wiki/Mathematical_proof',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    11769: {
        'mean': 0.25814898095259414,
        'variance': 0.42955861945985335,
        'timestamp': 2500723.0,
        'title': 'Ground state',
        'description': 'Lowest energy level of a quantum system',
        'url': 'https://en.wikipedia.org/wiki/Ground_state',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    23578: {
        'mean': 0.25814898095259414,
        'variance': 0.42955861945985335,
        'timestamp': 2500723.0,
        'title': 'Sampling (statistics)',
        'description': 'Selection of data points in statistics.',
        'url': 'https://en.wikipedia.org/wiki/Sampling_(statistics)',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    8504: {
        'mean': 0.26321005109549517,
        'variance': 0.43195361485503525,
        'timestamp': 2500723.0,
        'title': 'Electron',
        'description': 'Elementary particle with negative charge',
        'url': 'https://en.wikipedia.org/wiki/Electron',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    18534: {
        'mean': 0.26321005109549517,
        'variance': 0.43195361485503525,
        'timestamp': 2500723.0,
        'title': 'Nuclear magnetic resonance',
        'description': 'Spectroscopic technique based on change of nuclear spin state',
        'url': 'https://en.wikipedia.org/wiki/Nuclear_magnetic_resonance',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    17824: {
        'mean': 0.2632100510954952,
        'variance': 0.43195361485503525,
        'timestamp': 2500723.0,
        'title': 'Nanotechnology',
        'description': 'Field of applied science addressing the control of matter on atomic and (supra)molecular scales',
        'url': 'https://en.wikipedia.org/wiki/Nanotechnology',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    7636: {
        'mean': 0.15216284805465316,
        'variance': 0.44223963714418435,
        'timestamp': 2500723.0,
        'title': 'Discrete space',
        'description': 'Type of topological space',
        'url': 'https://en.wikipedia.org/wiki/Discrete_space',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    21311: {
        'mean': 0.0832324961055529,
        'variance': 0.4570580981927035,
        'timestamp': 2500723.0,
        'title': 'Prior probability',
        'description': 'Distribution of an uncertain quantity',
        'url': 'https://en.wikipedia.org/wiki/Prior_probability',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    11972: {
        'mean': 0.0967238419245315,
        'variance': 0.45310378894942144,
        'timestamp': 2500723.0,
        'title': 'Handwriting recognition',
        'description': 'Ability of a computer to receive and interpret intelligible handwritten input',
        'url': 'https://en.wikipedia.org/wiki/Handwriting_recognition',
        'history': deque([(0.0, 0.5, 2500723.0)])
    },
    16086: {
        'mean': 0.23919560839159543,
        'variance': 0.4324989154596735,
        'timestamp': 2597189.0,
        'title': 'Marginal likelihood',
        'description': '',
        'url': 'https://en.wikipedia.org/wiki/Marginal_likelihood',
        'history': deque([(0.0, 0.5, 2597189.0)])
    },
    21456: {
        'mean': 0.23919560839159543,
        'variance': 0.4324989154596735,
        'timestamp': 2597189.0,
        'title': 'Product rule',
        'description': 'Formula for the derivative of a product',
        'url': 'https://en.wikipedia.org/wiki/Product_rule',
        'history': deque([(0.0, 0.5, 2597189.0)])
    },
    5518: {
        'mean': 0.23919560839159543,
        'variance': 0.4324989154596735,
        'timestamp': 2597189.0,
        'title': 'Conditional probability',
        'description': 'Probability of an event occurring, given that another event has already occurred',
        'url': 'https://en.wikipedia.org/wiki/Conditional_probability',
        'history': deque([(0.0, 0.5, 2597189.0)])
    }
}


def dict_to_knowledge(knowledge_dict):
    new_knowledge_dict = {}
    for id, kc_dict in knowledge_dict.items():
        kc = HistoryAwareKnowledgeComponent(**kc_dict)
        new_knowledge_dict[id] = kc
    return Knowledge(new_knowledge_dict)


knowledge = dict_to_knowledge(knowledge_dict)
