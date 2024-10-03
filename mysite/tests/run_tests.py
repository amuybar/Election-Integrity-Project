import os
import sys

# Add the directory containing your Django project to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # Adjust path as necessary

from django.core.management import call_command

# Set the Django settings module if not already set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Ensure you are running this script in the Django context
import django
django.setup()

def run_tests():
    # List of test commands to run
    test_commands = [
        'users.tests.test_views',
        'users.tests.test_models', 
        # 'users.tests.test_forms', 
        # Add more test commands as needed
        'reporting.tests',
        # 'reporting.tests.test_models',
        # 'reporting.tests.test_forms',
        # Add more test commands as needed
        # 'admin.tests.test_views',
        # 'admin.tests.test_models',
        # 'admin.tests.test_forms',
        # Add more test commands as needed
        
    ]

    for command in test_commands:
        print(f"Running tests for: {command}")
        call_command('test', command, verbosity=2)

if __name__ == "__main__":
    run_tests()
