
def serve_tea(flavor):
    try:
        print(f"Preparing {flavor} tea ....")
        if flavor == "unknown":
            raise ValueError("We don't have that flavor")
    except ValueError as e:
        print(f"Error {e}")
    else:
        print(f"{flavor} tea is served")

    finally:
        print("Next customer please")

serve_tea("lemon")
print("------")
serve_tea("unknown")
print("------")
