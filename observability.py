#log each step to a list:return full log
def agent_loop():
    log = []

    # Step 1
    log.append("Step 1: Observe")

    # Step 2
    log.append("Step 2: Decide")

    # Step 3
    log.append("Step 3: Act")

    return log


result = agent_loop()

print("Full Log:")
for entry in result:
    print(entry)
