FEATURE_FLAGS = {
    'ENABLE_TEMPLATE_PROCESSING': True,
}

ENABLE_PROXY_FIX = True
SECRET_KEY = 'YOUR_OWN_RANDOM_GENERATED_STRING'

# Define categorical color schemes
EXTRA_CATEGORICAL_COLOR_SCHEMES = [
    {
        "id": 'viva_colors1',
        "description": 'Viva custom color palette',
        "label": 'Viva Colors 1',
        "colors": [
            '#e30613', '#eb2a32', '#f24d51', '#f86f70', '#ff9190',
            '#ffb3af', '#ffd5ce', '#fff7ee', '#ffffff', '#b4b4b4', '#f1f1f1'
        ]
    },
    {
        "id": 'viva_colors2',
        "description": 'Viva custom color palette',
        "label": 'Viva Colors 2',
        "colors": [
            '#e30613', '#c9141b', '#a82122', '#881b25', '#701326',  # More contrasting reds
            '#ffb3af', '#ff9190', '#ffd5ce', '#fff7ee', '#ffffff'
        ]
    },
    {
        "id": 'inferno_colors',
        "description": 'Inferno color palette',
        "label": 'Inferno',
        "colors": [
            '#000004', '#1f0c48', '#550f6d', '#88226a', '#a83655',
            '#cb4721', '#e95f0a', '#fca50a', '#f6d746', '#fcffa4'
        ]
    },
    {
        "id": 'viridis_colors',
        "description": 'Viridis color palette',
        "label": 'Viridis',
        "colors": [
            '#440154', '#482777', '#3f4a8a', '#31678e', '#26838f',
            '#1f9d8a', '#6cce5a', '#b6de2b', '#fee825'
        ]
    },
    {
        "id": 'viva_colors3',
        "description": 'Viva custom red, black, and grey palette',
        "label": 'Viva Colors 3',
        "colors": [
            '#e30613', # Bright red
            '#a8000b', # Darker red
            '#730000', # Deep red
            '#333333', # Dark grey
            '#cccccc'  # Light grey
        ]
    }
]

# Optional: Set the default color scheme to use your custom colors
DEFAULT_COLOR_SCHEME = 'viva_colors'


