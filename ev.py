events={}

PLR_DMG="player_damage"

def emit(ev_type, data={}):
    global events
    if not ev_type in events:
        events[ev_type]=[]
    events[ev_type].append(data)

def poll(ev_type):
    if not ev_type in events:
        return []
    ev = events[ev_type]
    del events[ev_type]
    return ev
