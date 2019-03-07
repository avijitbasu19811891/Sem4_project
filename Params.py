GlobalNNParamChoices = {
    'nb_neurons': [64, 128, 256, 512],
    'nb_layers': [1, 2, 3, 5, 7],
    'activation': ['relu', 'elu', 'tanh', 'sigmoid'],
    'optimizer': ['rmsprop', 'adam', 'sgd', 'adagrad',
                  'adadelta', 'adamax', 'nadam'],
}

def RandomChoiceFn (key, paramsChoice):
    return random.choice(paramsChoice[key])


Generations = 2  # Number of times to evole the population.
Population = 20  # Number of networks in each generation.
TopBreedPercent = 15
FitnessPopulationPercent = 70
DataSetFilePath = "./ml_data/"

LoadPartial=1
NumOfFileToLoad = 500
