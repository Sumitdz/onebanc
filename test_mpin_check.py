from mpin_check import evaluate_mpin_strength, load_common_mpin_list

def run_tests():
    common_mpins = load_common_mpin_list()

    test_data = [
        #Format: (mpin, user_data_dict, expected_strength, expected_reasons)

        ("1234", {}, "WEAK", ["COMMONLY_USED"]),
        ("1111", {}, "WEAK", ["COMMONLY_USED"]),
        ("0201", {"dob": "02-01-1998"}, "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF"]),
        ("001230", {"spouse_dob": "30-12-2000"}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("10102020", {"anniversary": "10-10-2020"}, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("0201", {
            "dob": "02-01-1998",
            "spouse_dob": "25-12-2001",
            "anniversary": "01-02-2020"
        }, "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_ANNIVERSARY"]),
        ("020198", {"dob": "02-01-1998"}, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("849392", {"dob": "02-01-1998"}, "STRONG", []),
        ("593482", {"dob": "05-05-2000", "spouse_dob": "15-11-2001", "anniversary": "20-07-2020"}, "STRONG", []),
        ("432789", {"dob": "30-06-1990", "spouse_dob": "20-04-1991", "anniversary": "01-01-2000"}, "STRONG", []),
        ("2512", {"spouse_dob": "25-12-1999"}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("3099", {"dob": "09-03-1999"}, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("1998", {"dob": "02-01-1998"}, "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF"]),
        ("123099", {"spouse_dob": "30-12-1999"}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("021298", {
            "dob": "02-12-1998",
            "spouse_dob": "02-12-1998",
            "anniversary": "02-12-1998"
        }, "WEAK", ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]),
        ("729384", {}, "STRONG", []),
        ("1506", {"spouse_dob": "15-06-2001"}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("1020", {"anniversary": "15-10-2020"}, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("6482", {"dob": "09-03-1989", "spouse_dob": "07-07-1990", "anniversary": "09-09-2001"}, "STRONG", []),
        ("991225", {"spouse_dob": "25-12-1999"}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("736291", {"dob": "05-05-1995", "spouse_dob": "06-06-1996", "anniversary": "07-07-2000"}, "STRONG", []),
        ("200711", {"anniversary": "20-07-2011"}, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("0102", {"dob": "02-01-1998"}, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("9912", {"spouse_dob": "20-12-1999"}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"])
    ]

    passed = 0
    for i, (mpin, user_data, expected_strength, expected_reasons) in enumerate(test_data, 1):
        result = evaluate_mpin_strength(mpin, user_data, common_mpins)

        if result["strength"] == expected_strength and set(result["reasons"]) == set(expected_reasons):
            print(f"✔ Test Case {i}: PASSED")
            passed += 1
        else:
            print(f"✖ Test Case {i}: FAILED")
            print(f"   Input MPIN: {mpin}")
            print(f"   User Data : {user_data}")
            print(f"   Expected  : Strength={expected_strength}, Reasons={expected_reasons}")
            print(f"   Got       : Strength={result['strength']}, Reasons={result['reasons']}")

    print(f"\n Summary: {passed}/{len(test_data)} test cases passed.")

if __name__ == "__main__":
    run_tests()
