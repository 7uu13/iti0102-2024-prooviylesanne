def parse_network_connections(connections: str) -> dict:
    # my solution for the exercise
    
    if not connections:
        return {}

    result_dict = {}

    for device in connections.split(","):
        device_names = device.split(":")
        l, r = 0, 1

        while r <= len(device_names) - 1:
            if device_names[l] not in result_dict:
                result_dict[device_names[l]] = [device_names[r]]
            else:
                if device_names[r] not in result_dict[device_names[l]]:
                    result_dict[device_names[l]].append(device_names[r])
            l += 1
            r += 1

    return result_dict