import json
from pathlib import Path
from faker import Faker
from cnfig import DATA_DIR



def get_test_data():
    """Checks for custom data first. If empty or missing, falls back to Faker."""

    custom_file = DATA_DIR / "user_data.json"

    # 1. Check if the file actually exists AND is not completely empty
    if custom_file.exists() and custom_file.stat().st_size > 0:
        try:
            with open(custom_file, "r") as f:
                custom_data = json.load(f)

            # 2. Safety check to make sure it has the right JSON structure
            if "valid_user" in custom_data:
                print(f"\n[INFO] 🛠️ Overriding Faker: Using manual data from user_data.json")
                return custom_data

        except json.JSONDecodeError:
            # If someone left a typo in the JSON (like a missing comma), catch it
            print("\n[WARNING]  user_data.json is corrupted or invalid! Falling back to Faker.")

    # 3. If file is missing, empty, or broken, generate fake data
    print("\n[INFO] No custom data found. Generating a random fake user.")
    return generate_and_archive_user()

def generate_and_archive_user():
    """Generates random data, archives the old user, and saves the new one."""
    fake = Faker()

    # Path logic (updated slightly since this file is now in the 'utils' folder)
    data_dir = Path(__file__).parent.parent / "data"
    users_file = data_dir / "users.json"
    used_data_file = data_dir / "used_data.json"

    data_dir.mkdir(exist_ok=True)

    # Archive old data
    if users_file.exists():
        try:
            with open(users_file, "r") as f:
                old_data = json.load(f)
            with open(used_data_file, "a") as used_f:
                used_f.write(json.dumps(old_data) + "\n")
        except json.JSONDecodeError:
            pass

    # Generate new data
    random_password = fake.password(length=12, special_chars=True, digits=True, upper_case=True)
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

    # Overwrite users.json
    with open(users_file, "w") as f:
        json.dump(new_data, f, indent=4)

    return new_data