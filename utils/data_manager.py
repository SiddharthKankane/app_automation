import json
from pathlib import Path
from faker import Faker
from cnfig import DATA_DIR


def get_existing_user():
    """Use this for direct login flows. It reads existing data without generating a new user."""
    custom_file = DATA_DIR / "user_data.json"
    generated_file = Path(__file__).parent.parent / "data" / "users.json"

    if custom_file.exists() and custom_file.stat().st_size > 0:
        try:
            with open(custom_file, "r") as f:
                custom_data = json.load(f)
            if "valid_user" in custom_data:
                return custom_data
        except json.JSONDecodeError:
            pass

    if generated_file.exists() and generated_file.stat().st_size > 0:
        try:
            with open(generated_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass

    return get_new_user()


def get_new_user():
    """Use this for fresh registration flows. It appends the current user to used_data on a new line,

    then overwrites users.json with fresh credentials.
    """
    fake = Faker()
    data_dir = Path(__file__).parent.parent / "data"
    users_file = data_dir / "users.json"
    used_data_file = data_dir / "used_data.json"

    data_dir.mkdir(exist_ok=True)

    # 1. Read the old data from users.json and append it to used_data.json on a clean new line
    if users_file.exists() and users_file.stat().st_size > 0:
        try:
            with open(users_file, "r") as f:
                old_data = json.load(f)

            # Open in append mode ('a') and explicitly add a newline character at the end
            with open(used_data_file, "a") as used_f:
                used_f.write(json.dumps(old_data) + "\n")
        except json.JSONDecodeError:
            pass  # Avoid crashing if the file contains corrupted JSON fragments

    # 2. Generate brand new data for the fresh registration flow
    random_password = fake.password(length=12, special_chars=False, digits=True, upper_case=True)
    new_data = {
        "valid_user": {
            "name": fake.user_name(),
            "email": fake.email(),
            "phone": fake.numerify(text="##########"),
            "location": fake.city(),
            "password": random_password,
            "confirm_password": random_password
        }
    }

    # 3. Completely overwrite users.json with the new data block
    with open(users_file, "w") as f:
        json.dump(new_data, f, indent=4)

    return new_data