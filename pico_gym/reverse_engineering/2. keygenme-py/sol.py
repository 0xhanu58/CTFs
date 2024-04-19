import hashlib

username_trial = "GOUGH"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

a = [4, 5, 3, 6, 2, 7, 1, 8]

for i in a:
    key_part_static1_trial += hashlib.sha256(username_trial.encode()).hexdigest()[i]

key_part_static1_trial += key_part_static2_trial
print(key_part_static1_trial)