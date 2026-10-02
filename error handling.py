#handle invalid action:return error dict
def handle_action(action):
    if action == "start":
        return {"status": "success"}
    else:
        return {"status": "error", "message": "Invalid action"}


result = handle_action("stop")
print(result)