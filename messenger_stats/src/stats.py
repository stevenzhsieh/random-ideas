import json

reacts = set()

emojiNames = {
    '\u00f0\u009f\u0091\u008e': 'thumbs_down',
    '\u00f0\u009f\u0098\u00a0': 'angry',
    '\u00f0\u009f\u0098\u008d': 'heart',
    '\u00f0\u009f\u0091\u008d': 'thumbs_up',
    '\u00f0\u009f\u0098\u0086': 'funny',
    '\u00f0\u009f\u0098\u00a2': 'cry',
    '\u00f0\u009f\u0098\u00ae': 'surprise'
}

"""
Open file and return as JSON
"""
def get_msgs():
    with open('./message.json') as jsonFile:
        return json.load(jsonFile)

msgs = get_msgs()

# Print participant names
names = list(map(lambda x: x['name'], msgs['participants']))
print("Participants:", ", ".join(names))

# Set up dicts
responseTimes = dict((name, []) for name in names)
numMsgs = dict((name, 0) for name in names)
msgLengths = dict((name, []) for name in names)
reacts = dict((name, {}) for name in names)
for name in reacts.keys():
    reacts[name] = dict((emojiNames[emoji], 0) for emoji in emojiNames.keys())

# Parse all messages
for msg in msgs['messages']:

    sender = msg['sender_name']
    text = msg['content']

    # Record for number of messages
    numMsgs[sender] += 1

    # Record message length
    length = len(text.split())
    msgLengths[sender].append(length)

    # Record reacts
    reactions = msg.get('reactions', [])
    for reaction in reactions:
        actor = reaction['actor']
        emoji = emojiNames[reaction['reaction']]
        reacts[actor][emoji] += 1

# Calculate average length
avgMsgLength = {}
for name in msgLengths:
    avgMsgLength[name] = sum(msgLengths[name])/len(msgLengths[name])

print(numMsgs)
print(avgMsgLength)
for name in reacts.keys():
    print(name)
    print(reacts[name])
