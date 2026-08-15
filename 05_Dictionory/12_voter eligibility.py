def check_eligibility(voter_data):
    eligibles = {}

    for key,value in voter_data.items():
        if value >= 18:
            eligibles[key] = value

    return eligibles


voter_data = {
    "VoterID_001": 25,
    "VoterID_002": 17,
    "VoterID_003": 55,
    "VoterID_004": 18,
    "VoterID_005": 16
}

print(check_eligibility(voter_data))