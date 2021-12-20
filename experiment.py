def get_experiment(elements):
    experiment = []

    for e in elements:
        experiment.append(e.text)

    experiment[1] = experiment[1].replace("\n", "")
    experiment[4] = experiment[4].replace("\n", " ")

    return experiment
