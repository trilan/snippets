DEFAULT_SETTINGS = {
    'SITE_NAME': 'Code Snippets',
    'SITE_URL': '',
    'REPOSITORY_PATH': 'snippets',
    'OUTPUT_PATH': 'output',
}


def get_settings(local_settings, default_settings=DEFAULT_SETTINGS):
    settings = default_settings.copy()
    for key, value in local_settings.items():
        if key.isupper():
            settings[key] = value
    return settings


def get_settings_from_file(filepath, default_settings=DEFAULT_SETTINGS):
    module_globals = {}
    execfile(filepath, module_globals)
    return get_settings(module_globals, default_settings)
