def clean_metadata(key, value):
    """Clean metadata keys and values before inserting into the database."""
    clean_key = (
        key.strip().lower() if key else None
    )  # Remove leading/trailing whitespace and lower case the key for consistency

    clean_value = value.strip() if value else None  # Remove leading/trailing whitespace

    return clean_key, clean_value


def validate_metadata(clean_key, added_metadata, reserved_keys):
    """Check for conflicts between user-provided metadata and reserved keys."""
    if clean_key in reserved_keys:
        return (
            False,
            f'"{clean_key}" is a reserved metadata key. Please choose a different key.',
        )
    elif clean_key in added_metadata:
        return (
            False,
            f'Duplicate metadata key: "{clean_key}". Please ensure all metadata keys are unique.',
        )
    else:
        return True, None
