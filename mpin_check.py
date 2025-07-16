import datetime

#Load common MPINs from file 
def load_common_mpin_list(filename="common_mpin_list.txt"):
    with open(filename, "r") as file:
        return set(line.strip() for line in file if line.strip())

#Check if MPIN is commonly used
def is_common_mpin(mpin, common_mpins):
    return mpin in common_mpins

#Generate demographic patterns based on given date
def generate_patterns(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
    except:
        return []
    day = date.strftime("%d")
    month = date.strftime("%m")
    year_short = date.strftime("%y")
    year_full = date.strftime("%Y")

    patterns = [
        day + month,
        month + day,
        year_short + month,
        month + year_short,
        day + year_short,
        year_short + day,
        year_full[-2:] + day,
        day + year_full[-2:],
        day + month + year_short,
        month + day + year_short,
        day + month + year_full[-2:]
    ]

    #Add 6 digit combinations for longer MPINs
    patterns += [
        day + month + year_full[-2:],
        year_full + month + day,
        month + day + year_full,
        year_full + day + month
    ]

    return patterns

#Check strength and reasons
def evaluate_mpin_strength(mpin, user_data, common_mpins):
    reasons = []

    if is_common_mpin(mpin, common_mpins):
        reasons.append("COMMONLY_USED")

    if 'dob' in user_data:
        if mpin in generate_patterns(user_data['dob']):
            reasons.append("DEMOGRAPHIC_DOB_SELF")

    if 'spouse_dob' in user_data:
        if mpin in generate_patterns(user_data['spouse_dob']):
            reasons.append("DEMOGRAPHIC_DOB_SPOUSE")

    if 'anniversary' in user_data:
        if mpin in generate_patterns(user_data['anniversary']):
            reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    strength = "WEAK" if reasons else "STRONG"
    return {"strength": strength, "reasons": reasons}
