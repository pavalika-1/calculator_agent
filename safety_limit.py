def observe():
    return "ready"


def decide(observation):
    if observation == "ready":
        return "success"
    return "retry"


def act(decision):
    return decision


def agent_loop():
    max_iters = 10
    for _ in range(max_iters):
        observation = observe()
        decision = decide(observation)
        if decision == "success":
            return "success"
        act(decision)
    return "failure"
